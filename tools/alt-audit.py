#!/usr/bin/env python3
"""Alt-szoveg audit: <img> tag-ek alt attributum nelkul a build-kimenetben."""
import re, sys, glob, os

root = sys.argv[1] if len(sys.argv) > 1 else 'public'
missing = []
empty = 0
total = 0
for f in glob.glob(os.path.join(root, '**/*.html'), recursive=True):
    s = open(f, errors='ignore').read()
    for m in re.finditer(r'<img\b[^>]*>', s):
        total += 1
        tag = m.group(0)
        am = re.search(r'alt="([^"]*)"', tag)
        sm = re.search(r'src="([^"]*)"', tag)
        src = sm.group(1) if sm else '?'
        if am is None:
            missing.append((f.replace(root, ''), src))
        elif am.group(1) == '':
            empty += 1

print(f'osszes img: {total}, ures (dekorativ) alt: {empty}, HIANYZO alt: {len(missing)}')
for f, src in missing[:40]:
    print('  ', f, '<-', src[:90])
