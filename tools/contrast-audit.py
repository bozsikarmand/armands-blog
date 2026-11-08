#!/usr/bin/env python3
"""WCAG 2.2 AAA kontraszt-audit a temak palettaibol.

Kiolvassa a _dark/_monolight tema-map-eket, es kiszamolja a WCAG
kontraszt-egyutthatokat a szoveg/hatter parokra.
AAA: normal szoveg 7:1, nagy szoveg 4.5:1, UI-elemek (1.4.11) 3:1.
"""
import re, sys

def hex_to_rgb(h):
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))

def lum(rgb):
    def f(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (f(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(c1, c2):
    l1, l2 = lum(hex_to_rgb(c1)), lum(hex_to_rgb(c2))
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)

def load_theme(path, varname):
    s = open(path).read()
    m = re.search(re.escape(varname) + r':\s*\((.*?)\);', s, re.DOTALL)
    body = m.group(1)
    out = {}
    for km in re.finditer(r'([a-z0-9-]+):\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|[a-z-]+\([^)]*\))', body):
        out[km.group(1)] = km.group(2)
    return out

# scss fuggvenyok egyszerusitese: lighten/darken around a hex
def simplify(v, ref):
    m = re.match(r'(lighten|darken)\((#[0-9a-fA-F]{6}),\s*([0-9.]+)%\)', v)
    if not m:
        return v if v.startswith('#') and len(v) in (4, 7) else None
    fn, hexv, pct = m.group(1), m.group(2), float(m.group(3))
    rgb = [int(hexv[i:i+2], 16) for i in (1, 3, 5)]
    f = pct / 100.0
    if fn == 'lighten':
        rgb = [round(c + (255 - c) * f) for c in rgb]
    else:
        rgb = [round(c * (1 - f)) for c in rgb]
    return '#%02x%02x%02x' % tuple(rgb)

# szoveg kulcs -> hatter kulcs parok (kulcs, hatterkulcs, tipus)
PAIRS = [
    ('body-color', 'body-background-color', 'normal'),
    ('title-color', 'body-background-color', 'nagy'),
    ('meta-color', 'body-background-color', 'normal'),
    ('link', 'body-background-color', 'normal'),
    ('link-hover', 'body-background-color', 'normal'),
    ('navbar-title-color', 'navbar-background-color', 'normal'),
    ('navbar-title-hover-color', 'navbar-background-color', 'normal'),
    ('navbar-title-active-color', 'navbar-background-color', 'normal'),
    ('footer-color', 'footer-background-color', 'normal'),
    ('dropdown-item-color', 'dropdown-content-background-color', 'normal'),
    ('dropdown-item-hover-color', 'dropdown-item-hover-background-color', 'normal'),
    ('sidebar-title-color', 'body-background-color', 'nagy'),
    ('sidebar-li-color', 'body-background-color', 'normal'),
    ('taxo-title-color', 'body-background-color', 'nagy'),
    ('taxo-num-color', 'taxo-num-background-color', 'normal'),
    ('taxo-tags-color', 'taxo-tags-background-color', 'normal'),
    ('taxo-categories-color', 'taxo-categories-background-color', 'normal'),
    ('breadcrumb-item-color', 'breadcrumb-background-color', 'normal'),
    ('breadcrumb-item-active-color', 'breadcrumb-background-color', 'normal'),
    ('list-header-title-color', 'body-background-color', 'nagy'),
    ('figcaption-color', 'body-background-color', 'normal'),
    ('single-header-title-color', 'body-background-color', 'nagy'),
    ('single-contents-title-color', 'body-background-color', 'nagy'),
    ('related-header-title-color', 'body-background-color', 'nagy'),
    ('pagination-link-color', 'pagination-background-color', 'normal'),
    ('pagination-number-color', 'pagination-background-color', 'normal'),
    ('terms-title-color', 'body-background-color', 'nagy'),
    ('terms-tags-color', 'body-background-color', 'normal'),
    ('toc-title-color', 'body-background-color', 'normal'),
    ('toc-label-color', 'body-background-color', 'normal'),
    ('search-color', 'search-background-color', 'normal'),
    ('search-placeholder-color', 'search-background-color', 'normal'),
    ('search-icon-color', 'search-background-color', 'normal'),
    ('search-content-color', 'search-content-background-color', 'normal'),
    ('archive-meta-color', 'body-background-color', 'normal'),
    ('archive-type-color', 'archive-type-background-color', 'normal'),
    ('contact-input-color', 'contact-input-background-color', 'normal'),
    ('gtt-color', 'gtt-background-color', 'normal'),
    ('social-icon-color', 'footer-background-color', 'normal'),
    ('burger-menu-color', 'navbar-background-color', 'normal'),
    ('single-blockquote-border-color', 'body-background-color', 'ui'),
    ('hr-color', 'body-background-color', 'ui'),
    ('search-border-color', 'search-background-color', 'ui'),
    ('navbar-border-bottom-color', 'navbar-background-color', 'ui'),
    ('dropdown-border-top-color', 'dropdown-content-background-color', 'ui'),
    ('pagination-disabled-color', 'pagination-background-color', 'normal'),
]
REQ = {'normal': 7.0, 'nagy': 4.5, 'ui': 3.0}

themes = {
    'dark': ('themes/armands-blog/assets/sass/themes/_dark.scss', '$dark'),
    'monolight': ('themes/armands-blog/assets/sass/themes/_monolight.scss', '$monolight'),
}

total_fail = 0
for name, (path, varname) in themes.items():
    t = load_theme(path, varname)
    print(f'\n=== {name} ===')
    fails = 0
    for key, bgkey, typ in PAIRS:
        v = t.get(key)
        bg = t.get(bgkey)
        if v is None or bg is None:
            print(f'  ?  {key}: hianyzik ({v} / {bg})')
            continue
        vc = simplify(v, t)
        bgc = simplify(bg, t)
        if not vc or not bgc:
            print(f'  ?  {key}: ertek nem ertelmezheto: {v}')
            continue
        r = ratio(vc, bgc)
        req = REQ[typ]
        mark = 'OK ' if r >= req else 'BUÉK'
        if r < req:
            fails += 1
        print(f'  {mark} {key:42s} {r:5.2f}:1 (kell {req}:1)  {vc} on {bgc}')
    print(f'  --> {fails} bukott par')
    total_fail += fails
print(f'\nOSSZESEN bukott parok: {total_fail}')

# ---------------- AUTOJAVASLAT mod ----------------
import colorsys

def rgb_to_hsl(r, g, b):
    # bemenet 0-1 skala (hex_to_rgb kimenete)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, s, l

def hsl_to_hex(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return '#%02x%02x%02x' % (round(r*255), round(g*255), round(b*255))

def fix_color(fg, bg, req):
    """Fg szint beallitasa, amig a kontraszt nem eleg (L igazitas, hue/S megtartva)."""
    frgb = hex_to_rgb(fg)
    brgb = hex_to_rgb(bg)
    h, s, l = rgb_to_hsl(*frgb)
    blum = lum(brgb)
    def ok(lv):
        c = hsl_to_hex(h, s, lv)
        l1, l2 = lum(hex_to_rgb(c)), blum
        if l1 < l2: l1, l2 = l2, l1
        return (l1 + 0.05) / (l2 + 0.05) >= req + 0.15
    # irany: ha a fg sotetebb a bgnel, sotetitunk; kulonben vilagositunk
    if lum(frgb) < blum:
        # sotetites: az eredetihez legkozelebbi (legvilagosabb) atmeno szint
        lo, hi = 0.0, l
        while hi - lo > 0.002:
            mid = (lo + hi) / 2
            if ok(mid): lo = mid
            else: hi = mid
        return hsl_to_hex(h, s, lo)
    else:
        # vilagositas: az eredetihez legkozelebbi (legsotetebb) atmeno szint
        lo, hi = l, 1.0
        while hi - lo > 0.002:
            mid = (lo + hi) / 2
            if ok(mid): hi = mid
            else: lo = mid
        return hsl_to_hex(h, s, hi)

if '--suggest' in sys.argv:
    print('\n\n===== AUTOJAVASLATOK =====')
    for name, (path, varname) in themes.items():
        t = load_theme(path, varname)
        print(f'\n--- {name} ---')
        for key, bgkey, typ in PAIRS:
            v, bg = t.get(key), t.get(bgkey)
            if not v or not bg: continue
            vc, bgc = simplify(v, t), simplify(bg, t)
            if not vc or not bgc: continue
            if ratio(vc, bgc) < REQ[typ]:
                fix = fix_color(vc, bgc, REQ[typ])
                print(f'{name}:{key}: {vc} -> {fix}')
