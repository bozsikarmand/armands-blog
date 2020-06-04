---
author: bozsikarmand
comments: true
date: 2015-09-09 16:01:09+00:00
layout: post
link: https://blog.bozsikarmand.hu/2015/09/09/microsoft-megvan-a-megoldas-a-windows-10-10049-es-verziojanak-hyper-v-anomaliaira/
slug: microsoft-megvan-a-megoldas-a-windows-10-10049-es-verziojanak-hyper-v-anomaliaira
title: 'Microsoft: Megvan a megoldás a Windows 10 10049-es verziójának Hyper-V anomáliáira'
wordpress_id: 260
categories:
- Hungarian
---

## A Microsoft ma több részletet közölt a Windows 10 legfrissebb publikus kiadásának virtualizációs képességét érintő hibáról


A szoftveróriás fejlesztés alatt álló rendszerének ugyan még csak tegnap jelent meg legújabb verziója, de úgy tűnik ez a kiadás sem mentes a bosszantó hibáktól. Azon felhasználók számára, akik az operációs rendszer beépített Hyper-V virtualizációs technológiáját használnák az új rendszeren, a frissítés nem ajánlott. A redmondi cég Hyper-V programmenedzsere, Ben Armstrong sietett a felhasználók segítségére, s az MSDN blog szekciójában közölte is a virtualizációs esköz hibáját orvosló megoldást.

Következzék bejegyzésének lényegi része, magyarra fordítva:





<blockquote>A fent említett hiba meggátolja, egy, a Hyper-V működéséhez feltétlenül szükséges meghajtó program operációs rendszerbe való bejegyzését, de ami a hiba lényegi részét adja az az, hogy mindez csak friss telepítés esetén van így. Amennyiben már van egy sikeresen feltelepített korábbi verziód, melyen engedélyezted a virtualizációs technológiánk, akkor minden probléma nélkül frissíthetsz az új kiadásra. Illetve ha a Project Spartan-t és a Hyper-V-t is szeretnéd használni az új rendszeren, a következőket kell tenned:

• Fel kell telepítened a Windows 10 egy korábbi verzióját
• Engedélyezned kell a Hyper-V-t
• Végül már csak frissítened kell az új 10049-es kiadásra</blockquote>





Egyébiránt az is megoldást jelenthet, ha a „gyors” kiadási ciklusról a „lassúra” váltasz, s megvárod, míg egy újabb kiadás nem érkezik, mely orvosolja a fenti problémát.

__Source:__ [Windows Central](http://www.windowscentral.com/microsoft-details-workaround-virtual-machine-bug-windows-10-build-10049)