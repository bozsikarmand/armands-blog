#!/usr/bin/env bash
set -u
i=0
for p in /en/ /hu/ /en/posts/hollow-talk/ /hu/posts/dijnyertes-muforditasom/ /en/about/ /en/tags/ /en/categories/; do
  i=$((i+1))
  f=/tmp/opencode/axe-page-$i.html
  timeout 120 chromium --headless --disable-gpu --no-sandbox --virtual-time-budget=25000 --force-prefers-reduced-motion \
    --dump-dom "http://localhost:8145$p" 2>/dev/null > "$f"
  PAGE="$p" FILE="$f" python3 - <<'PYEOF'
import os, re, html, json
s = open(os.environ['FILE'], errors='ignore').read()
m = re.search(r'<pre id="axe-out"[^>]*>(.*?)</pre>', s, re.DOTALL)
p = os.environ['PAGE']
if not m:
    print('=== %s: NINCS KIMENET (%d bájt)' % (p, len(s)))
else:
    try:
        d = json.loads(html.unescape(m.group(1)))
        v = d['violations']
        print('=== %s: %s' % (p, (str(len(v)) + ' violation') if v else 'TISZTA'))
        for x in v:
            print('   [%s] %s (%d) %s' % (x['impact'], x['id'], x['count'], x['help'][:85]))
            for smp in x['sample'][:2]:
                print('      ', smp.replace(chr(10), ' ')[:140])
    except Exception as e:
        print('=== %s: NEM JSON: %s' % (p, html.unescape(m.group(1))[:150]))
PYEOF
done
