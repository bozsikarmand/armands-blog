#!/usr/bin/env python3
"""axe-t injektalo statikus szerver: minden HTML-be beilleszti a futtatot.

Hasznalat: python3 tools/axe-serve.py <konyvtar> <port>
Ezutan: chromium --headless --dump-dom http://localhost:<port>/<oldal>
  -> a DOM-ban az <pre id="axe-out"> tartalmazza az eredmenyeket.
"""
import http.server, functools, sys, os

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else 'public'
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8145

RUNNER = """
<pre id="axe-out" style="display:none">PENDING</pre>
<script src="/axe.min.js"></script>
<script>
(async function () {
  var OUT = function (m) { document.getElementById('axe-out').textContent = m; };
  try {
    await new Promise(function (r) {
      if (document.readyState === 'complete') r();
      else window.addEventListener('load', r);
    });
    await new Promise(function (r) { setTimeout(r, 400); });
    var results = await axe.run(document, {
      runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'wcag2aaa', 'best-practice'] }
    });
    var out = { violations: results.violations.map(function (v) {
      return { id: v.id, impact: v.impact, help: v.help, count: v.nodes.length,
        sample: v.nodes.slice(0, 8).map(function (n) {
          var cd = null;
          try {
            var chk = (n.any && n.any[0]) || (n.all && n.all[0]);
            if (chk && chk.data) cd = { fg: chk.data.fgColor, bg: chk.data.bgColor, ratio: chk.data.contrastRatio, expected: chk.data.expectedContrastRatio };
          } catch (e) {}
          return { html: n.html.slice(0, 120), cd: cd };
        }) };
    })};
    OUT(JSON.stringify(out, null, 1));
  } catch (e) { OUT('HIBA: ' + e.message); }
})();
</script>
"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()
    def guess_type(self, path):
        if path.endswith('.js'):
            return 'text/javascript'
        return super().guess_type(path)
    def do_GET(self):
        if self.path == '/' or self.path.endswith('/') or self.path.endswith('.html'):
            # html kiszolgalas injekcioval
            rel = self.path.lstrip('/')
            if not rel or rel.endswith('/'):
                rel += 'index.html'
            fp = os.path.join(ROOT, rel)
            if os.path.isfile(fp):
                body = open(fp, errors='ignore').read()
                if '</body>' in body:
                    body = body.replace('</body>', RUNNER + '</body>')
                else:
                    body += RUNNER
                data = body.encode()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
                self.wfile.write(data)
                return
        super().do_GET()

http.server.ThreadingHTTPServer(('127.0.0.1', PORT), Handler).serve_forever()
