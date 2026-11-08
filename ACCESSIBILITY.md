# Akadálymentesség – WCAG 2.2 AAA

Ez a blog a **WCAG 2.2 AAA** szintű megfelelésre törekszik. Az oldal
minden felhasználói beállítása – a két téma (dark/monolight), a szövegterköz,
a nagyítás és a mozgáscsökkentés – a megfelelés része.

Nyilatkozat: [/en/accessibility](/en/accessibility/) ·
[/hu/accessibility](/hu/accessibility/)

## Eszközök (tools/)

| Eszköz | Mire való |
|---|---|
| `contrast-audit.py` | Mindkét téma összes szöveg/háttér párját ellenőrzi AAA szerint (jelenleg: **0 bukás**) |
| `axe-serve.py` | axe-core-t injektáló helyi szerver |
| `axe-scan.sh` | axe-futtatás az összes oldaltípuson (jelenleg: **0 violation**) |
| `alt-audit.py` | Alt-szöveg-ellenőrzés a build-kimeneten (jelenleg: **0 hiányzó alt**) |

Futtatás:

```bash
./tools/sync-theme.sh
hugo --destination /tmp/axe-site
cp <axe.min.js útvonal> /tmp/axe-site/   # egyszeri
python3 tools/axe-serve.py /tmp/axe-site 8145 &
./tools/axe-scan.sh
python3 tools/contrast-audit.py
python3 tools/alt-audit.py /tmp/axe-site
```

## Szerkesztői checklist (minden új poszthoz)

1. **Alt-szöveg** minden informatív képhez (`![leírás](...)` vagy
   `figure alt="..."`). Dekoratív képhez: üres alt.
2. **Értelmes link-szöveg** – soha „itt” vagy „kattints ide”. A külső linkek
   automatikusan jelölve lesznek („új lapon nyílik”).
3. **Fejlécsorrend**: a poszt címe H1, utána H2, H3… ne ugorj át szintet.
4. **Rövidítések**: a gyakoriak (HTML, CSS, UEFI…) automatikusan
   `<abbr>`-be kerülnek; új rövidítésnél bővítsd a
   `hugo-theme-armands-blog` repó `layouts/partials/abbr-content.html`
   szótárát.
5. **Videó**: `youtube` shortcode használata (`{{< youtube id >}}`) –
   címet és felirat-linket ad.
6. **Kontraszt**: ha új színt veszel fel a témában, futtasd a
   `contrast-audit.py`-t.

## Amit a rendszer automatikusan biztosít

- Egymain-landmark, „Ugrás a tartalomra”, fejléc-hierarchia
- AAA fókuszjelölés, 44×44 célméretek, billentyűzet-kezelhető dropdownok
- `aria-live` keresési találatok, `aria-pressed` témacsere
- reduced-motion alatt minden animáció kikapcsol
- 320px reflow, 200% nagyítás, felhasználói szövegterköz-támogatás

## Nem alkalmazható / dokumentált kivételek

- Beágyazott YouTube-videók feliratai/jelnyelve – harmadik fél tartalma
- Időzítés, belépés, többlépéses űrlapok – nincsenek az oldalon
- Olvasási szint (3.1.5) – szakmai/technikai tartalom; a nyilatkozatban
  rögzítve
