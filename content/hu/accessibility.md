---
title: Akadálymentességi nyilatkozat
date: 2026-11-08
slug: accessibility
---

Elkötelezett vagyok amellett, hogy az oldal mindenki számára – fogyatékkal
élő felhasználók részére is – hozzáférhető legyen, és folyamatosan javítom a
felhasználói élményt az elérhető szabványok alkalmazásával.

## Megfelelés szintje

Ez a weboldal a **Web Content Accessibility Guidelines (WCAG) 2.2 AAA
szintű** megfelelésére törekszik. Az irányelvek azt írják le, hogyan tehető
a webes tartalom hozzáférhetőbbé széles körű fogyatékossággal élő
felhasználók számára.

## Megtett intézkedések

- **Kontraszt**: minden szöveg megfelel a fokozott kontraszt-követelményeknek
  (7:1 normál, 4.5:1 nagy szöveg) mind a sötét, mind a világos témában,
  automatizált eszközzel ellenőrizve (`tools/contrast-audit.py`).
- **Billentyűzet**: minden interakció (navigáció, keresés, nyelv- és
  témacsere, menük) kizárólag billentyűzettel is működik.
- **Fókusz**: a jól látható fókuszjelölő megfelel a WCAG 2.2 AAA
  fókusz-megjelenési követelményeinek, és a fix fejléc sosem takarja el.
- **Képernyőfelolvasók**: szemantikai landmarkok, fejlécek, „Ugrás a
  tartalomra" link, címkék és státuszüzenetek segítik az asszisztív
  technológiákat; automatizált audit axe-core rendszerrel
  (`tools/axe-scan.sh`).
- **Alkalmazkodóképesség**: a tartalom 320&nbsp;px-en is átfolyik,
  ellenáll a 200%-os szövegnagyításnak, és tiszteletben tartja a
  felhasználói szövegterköz- és mozgáscsökkentési beállításokat.
- **Képek**: az informatív képekhez alternatív szöveg tartozik; a
  tisztán dekoratív képek e szerint vannak jelölve.
- **Nyelv**: az oldal nyelve meg van jelölve; nyelvválasztó a fejlécben és
  a láblécben is elérhető.
- **Mozgás**: animációk kikapcsolnak, ha a felhasználó csökkentett mozgást
  kér.

## Nem alkalmazható / harmadik féltől származó tartalom

- **Beágyazott videók** YouTube-on vannak tárolva; a feliratokat a
  lejátszó biztosítja. Harmadik féltől származó videók jelnyelvi
  tolmácsolása a kiadó ellenőrzésén kívül áll.
- **Időzített tartalom, belépés vagy többlépéses űrlap** nincs az oldalon.
- A régebbi bejegyzések külső, harmadik féltől származó erőforrásokra
  hivatkozhatnak, amelyek akadálymentességéért nem tudok felelni.

## Visszajelzés

Ha akadályba ütközik, kérem, jelezze, és a lehető leghamarabb orvoslom:

- E-mail: [hello@armands.site](mailto:hello@armands.site)
- A nyilatkozat utolsó frissítése: **2026-11-08**.
