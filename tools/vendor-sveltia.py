#!/usr/bin/env python3
"""Sveltia CMS vendorolasa a repoba + a helyi patch-ek ujraalkalmazasa.

Hasznalat:
    python3 tools/vendor-sveltia.py [verzio]      # pl.: 0.261.0 (alap: 0.261.0)

Mit csinal:
1. Letolti a @sveltia/cms dist/sveltia-cms.js-t a megadott verzioban
2. A bundle-bol kinyeri a fontsource font-URL-eket, letolti es lokalisra irja oket
3. A dinamikus import-alapot (LM) lokalis vendor-utvonalra allitja
4. Az exifr konyvtarat behozza a /admin/vendor/ ala (ha hianyozna)
5. Ellenorzi, hogy nem maradt-e tiltando kulso URL a bundle-ben

Az igy kepzett fajlok a szigoru CSP mellett is mukodnek; frissites utan
futtasd ujra ezt a scriptet (a patchek igy mindig visszakerulnek).
"""
import re, sys, os, urllib.request, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMIN = os.path.join(ROOT, 'static', 'admin')
VERSION = sys.argv[1] if len(sys.argv) > 1 else '0.261.0'

BUNDLE_URL = f'https://cdn.jsdelivr.net/npm/@sveltia/cms@{VERSION}/dist/sveltia-cms.js'
BUNDLE = os.path.join(ADMIN, 'sveltia-cms.js')

def download(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    print('  letöltés:', url)
    urllib.request.urlretrieve(url, dest)

print(f'== Sveltia CMS {VERSION} vendorolása ==')
download(BUNDLE_URL, BUNDLE)
s = open(BUNDLE, encoding='utf-8').read()

# 1) fontsource font-ok: letoltes + lokalisra iras
fonts = sorted(set(re.findall(r'https://cdn\.jsdelivr\.net/fontsource/fonts/[^\'"`\s)]+', s)))
name_map = {
    'material-symbols-outlined': 'material-symbols.woff2',
    'source-sans-3': 'source-sans-3.woff2',
    'noto-mono': 'noto-mono.woff2',
}
for url in fonts:
    m = re.search(r'/fonts/([a-z0-9-]+?)(?::vf)?@', url)
    fam = m.group(1) if m else 'egyeb'
    local = name_map.get(fam, fam + '.woff2')
    dest = os.path.join(ADMIN, 'fonts', local)
    if not os.path.exists(dest):
        download(url, dest)
    s = s.replace(url, f'/admin/fonts/{local}')
    print('  font:', fam, '->', local)

# 2) dinamikus import alap
old = 'LM=e=>{let t=`https://unpkg.com/${e}`'
if old in s:
    s = s.replace(old, 'LM=e=>{let t=`/admin/vendor/${e}`')
    print('  LM -> /admin/vendor/')

# 3) exifr
exifr = os.path.join(ADMIN, 'vendor', 'exifr', 'dist', 'lite.esm.mjs')
if not os.path.exists(exifr):
    download('https://unpkg.com/exifr@7.1.3/dist/lite.esm.mjs', exifr)

# 4) forrasterkep-hivatkozasok torlese
s = re.sub(r'\n?//# sourceMappingURL=[^\n]*', '', s)

open(BUNDLE, 'w', encoding='utf-8').write(s)

# 5) ellenorzes
leftover = sorted(set(re.findall(r'https://cdn\.jsdelivr\.net/[^\'"`\s)]+', s)))
leftover = [u for u in leftover if 'fontsource' in u]
allowed = {'https://unpkg.com/@sveltia/cms/package.json',
           'https://status-api.hostedstatus.com/1.0/status/5b36dc6502d06804c08349f7'}
bad = [u for u in re.findall(r'https://(?:unpkg\.com|cdn\.jsdelivr\.net)[^\'"`\s)]+', s)
       if u not in allowed]
print('== Kész. Tiltott maradt:', bad if bad else 'nincs ✓')
print('Következő lépés: git add static/admin && git commit -m "Update Sveltia CMS to', VERSION + '"')
