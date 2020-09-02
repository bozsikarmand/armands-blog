---
author: bozsikarmand
comments: true
date: 2015-09-10 12:26:39+00:00
layout: post
link: https://blog.bozsikarmand.hu/2015/09/10/az-ethernet-szabvany-attekintese-es-idorendi-fejlodese/
slug: az-ethernet-szabvany-attekintese-es-idorendi-fejlodese
title: Az Ethernet szabvány áttekintése és időrendi fejlődése
wordpress_id: 323
categories:
- Study
---

_Beadandó munkámban az Ethernet szabványt kívánom áttekinteni, a történelmi és technikai háttért figyelembe véve._

Az Ethernet a számítógépes hálózati technológiák családjába tartozó szabvány, mely helyi (LAN) és városi méretű (WAN) hálózatok összekötésére szolgál. Az Ethernet 1980-ban került bemutatásra, majd 1983-ban vált szabvánnyá IEEE 802.3 néven. Ettől kezdve a szabvány alapjaiban nem változott, csupán mindig a kor (egyre növekvő) igényeihez igazították. Változott a maximálisan kihúzható kábelhossz két gép közt, illetve az adatátviteli sebesség is jelentősen megnőtt az idők folyamán.

A szabvány megfelelőnek bizonyult, mely tényt az idő hivatott igazolni, ugyanis rövidesen az egyéb vezetékes technológiákat kiszorította a piacról (pl. token ring, FDDI, ARCNET). Később megjelent az igény a vezeték nélküli adattovábbításra (pl. Wi-Fi) mely az IEEE 802.11 nevet kapta.

Az Ethernet szabványokban sokféle kábelezési és jeltovábbítási ajánlást tettek az OSI (Open Systems Interconnection - Nyílt rendszerek összekapcsolása: ez egy olyan, általánosan alkalmazható tervezet, mely a világon előforduló összes hálózatra egyaránt érvényes) fizikai rétegére vonatkozóan. Az eredeti 10BASE5 Ethernet vastag koaxiális kábelt használt, míg az újabb szabványok (802.3i (1990)-től felfelé) már csavart érpárt illetve üvegszálas optikát. Ezen változásokat természetesen az aktív hálózati eszközök is lekövették (switch-ek, HUB-ok, routerek).

[caption id="attachment_331" align="aligncenter" width="300"][![koax](https://armands.blog/images/koax.gif)](https://armands.blog/images/koax.gif) Koax kábel felépítése[/caption]

[caption id="attachment_333" align="aligncenter" width="300"][![utp](https://armands.blog/images/utp.jpg)](https://armands.blog/images/utp.jpg) UTP kábel felépítése[/caption]

[caption id="attachment_334" align="aligncenter" width="300"][![Image191](https://armands.blog/images/Image191.gif)](https://armands.blog/images/Image191.gif) Optikai kábel[/caption]

[caption id="attachment_335" align="aligncenter" width="300"][![164963-Cisco-Small-Business-24-Port-10-100-Switch-with-Gigabit-Uplinks](https://armands.blog/images/cisco-switch.jpg)](https://armands.blog/images/cisco-switch.jpg) Cisco Switch[/caption]

[caption id="attachment_336" align="aligncenter" width="300"][![100_1891](https://armands.blog/images/100_1891.png)](https://armands.blog/images/100_1891.jpg) Cisco HUB[/caption]

[caption id="attachment_337" align="aligncenter" width="300"][![Cisco-1800](https://armands.blog/images/Cisco-1800.jpg)](https://armands.blog/images/Cisco-1800.jpg) Cisco Router[/caption]

A legelső (még szabadalmaztatás előtti, kísérleti) Ethernet szabvány 2,94 Mbit/s átvitelre volt képes, a jelenlegi leggyorsabb 100 Gbit/s-ra, míg 2017-re 400 Gbit/s-os elméleti maximumot igérnek.

Az Etherneten kommunikáló eszközök (mivel a folyamatos, egyszerre történő adatfogadásnak és feldolgozásnak technikai és adatbiztonsági akadályai vannak) kis egységekben, ún. framekben kommunikálnak. Minden frame tartalmazza a csomag cél és forráscímét, illetve egy hibaellenőrző rutint, mely figyeli, hogy nem sérült-e meg az adat továbbítás közben, s amennyiben igen, akkor a hibás csomagot újraküldi. Az OSI modell alapján az Ethernet szabvány az első két rétegben (fizikai és adatkapcsolati) nyújt szolgáltatásokat.

A szabvány (és annak alapján készült eszközök) kereskedelmi megjelenése óta jó példaként szolgál a visszafelé való kompatibilitás bemutatására. A használt 48 bites MAC címzés (ami 248 –on db címet jelent…), illetve az Ethernet csomagformátuma más hálózati protokollokra is hatással volt a későbbiekben.


## Történelmi háttér


Az Ethernet szabvány a Xerox PARC fejlesztette ki 1973-74 közt. A fejlesztést az ALOHAnet inspirálta, mely az egyik társszerző, Robert Metcalfe PhD munkájában is helyet kapott. Az ötlet első írásos emléke 1973 májusából való, s melyből megtudhatjuk, hogy az Ethernet elnevezés az éter angol elnevezéséből ([a]ether) származik, s melyet a következőképp definiált: „Mindenütt jelenlévő passzív közeg, mely elektromágneses hullámok továbbítására alkalmas”. 1975-ben a Xerox egy szabadalmi kérelmet nyújtott be, melyben Metcalfe-ot, David Boggs-t, Chuck Thacker-t illetve Butler Lampson-t jelölték meg a technológia kidolgozóiként. 1976-ban, miután a rendszer sikeresen összeállításra került a PARC-nél, Metcalfe és Boggs dolgozatának témája a technológia kifejlesztése lett.

Metcalfe 1979 nyarán elhagyta a Xeroxot, majd megalapította a 3Com-ot. Ezután meggyőzte a DEC-t, az Intelt illetve a Xeroxot, hogy dolgozzanak együtt, így téve az Ethernetet igazi szabvánnyá.
<table align="center">
<tbody>
<tr >

<td colspan="3" width="451">**                 A szabványok áttekintése időrendben    **
</td>
</tr>
<tr>

<td width="150" >_Szabvány_
</td>

<td width="150" >_Bevezetés_
</td>

<td width="150" >_Röviden_
</td>
</tr>
<tr>

<td width="150" >Kisérleti
</td>

<td width="150" >1972-78
</td>

<td width="150" >2,94Mbit/s, koax kábel
</td>
</tr>
<tr>

<td width="150" >Ethernet II/DIX
</td>

<td width="150" >1982
</td>

<td width="150" >10 Mbit/s, vastag koax
</td>
</tr>
<tr>

<td width="150" >IEEE 802.3
</td>

<td width="150" >1983
</td>

<td width="150" >10BASE5 - 10 Mbit/s, vastag koax
</td>
</tr>
<tr>

<td width="150" >802.3i
</td>

<td width="150" >1990
</td>

<td width="150" >10BASE-T, 10 Mbit/s, csavart érpár
</td>
</tr>
<tr>

<td width="150" >802.3u
</td>

<td width="150" >1995
</td>

<td width="150" >100BASE-T*/FX, 100 Mbit/s
</td>
</tr>
<tr>

<td width="150" >802.3ac
</td>

<td width="150" >1998
</td>

<td width="150" >Keretméret: 1522B
</td>
</tr>
<tr>

<td width="150" >802.3ab
</td>

<td width="150" >1999
</td>

<td width="150" >1000BASE-T, Gigabit Eth, csavart érpáron
</td>
</tr>
<tr>

<td width="150" >802.3ae
</td>

<td width="150" >2003
</td>

<td width="150" >10GBASE-*, 1 GBit/s üvegszálon
</td>
</tr>
<tr>

<td width="150" >802.3af
</td>

<td width="150" >2003
</td>

<td width="150" >


Power over Ethernet



</td>
</tr>
</tbody>
</table>
A fenti táblázatban a DIX a Digital/Intel/Xerox elnevezésből származik. Ezen kívül 48 bites cél- és forráscímzést, 16 bites EtherType-ot (mely az Ethernet keretbe csomagolt adat azonosítására alkalmas). Az eredeti szabvány specifikációja 1980 szeptemberében jelent meg „The Ethernet, A Local Area Network. Data Link Layer and Physical Layer Specifications” címmel, majd a második verzióé (Ethernet II:  Formal standardization efforts) 1982-ben. Ezt követte az IEEE802.3 szabvány publikálása 1983-ban.

Az Ethernet szabványnak két kihívója is akadt, - melyek többnyire zárt rendszerek voltak – a Token Ring és a Token Bus. Mivel az Ethernet hatalmas előnyei közé tartozott az olcsó előállíthatóság a csavart érpár használatának köszönhetően, így hamarosan kiszorította a piacról ellenfeleit, majd az 1980-as évek végére övé lett a domináns szerep. A 3Com 1981-ben kezdte el szállítani első 10 Mbit/s átvitelt tudó 3C100-as hálózati kártyáját, majd adaptereket is biztosított PDP-11/VAX/Multibus alapú Intel és Sun gépekhez.

Ezt követte a DEC Unibus-Ethernet adaptere, ezzel a cég teljes belső vállalati hálózatot épített ki, mely 1986-ra 10 000 hálózati csomópontot tartalmazott, így abban az időben övék volt a legnagyobb hálózat az egész világon. Az Ethernet szabvány fejlődése (főként a 10BASE-T megjelenése) ösztönzőleg hatott a processzorgyártók fejlesztési kedvére is, egyre gyorsabb lapkák jelentek meg, illetve az alsóbb kategóriás alaplapokon is elterjedt az Ethernet csatlakozó ezzel egy időben.

Az Ethernet azóta folytatja világhódító útját. Ma már – a folyamatos fejlesztéseknek köszönhetően nem csak asztali számítógépekben és munkaállomásokban található meg. Ipari felhasználása és a telekommunikációban betöltött szerepe is jelentős az egyre nagyobb adatátviteli sebesség miatt.


## Szabványosítási kérdések


1980 februárjában az Institute of Electrical and Electronics Engineers (IEEE) elindította a 802-es projektet mellyel a LAN-ok egységesítését kívánta elérni. A „DIX-csoport” (Gary Robinson [DEC], Phil Arst [Intel], Bob Printis [Xerox]) ekkor közszemlére bocsájtotta az ún. „kék könyvet” mely a CSMA/CD specifikációját tartalmazta, s amely később a LAN specifikáció egyik lehetséges jelöltje lett. A CSMA/CD mellett természetesen más alternatívák is szerepeltek, úgy, mint a General Motors-féle Token Bus, vagy az IBM gondozásában álló Token Ring. A felsorakoztatott technológiák és a mögöttük álló cégek erőviszonyai hamarosan vitába csaptak át a szabványosítás kérdésében. 1980 decemberében a csoport három alcsoportra bomlott, így lehetőség nyílt mindhárom technológia szabványosítására.


## Technológiai háttér


[caption id="attachment_324" align="aligncenter" width="300"][![iso-osi-tcp]((https://armands.blog/images/iso-osi-tcp.jpg)]((https://armands.blog/images/iso-osi-tcp.jpg) ISO/OSI/TCP[/caption]

Többször esett már szó az Ethernet fejlődéséről a korábbi oldalakon, azonban technológiai szempontból még nem vizsgáltuk meg. Mint korábban említettem, az Ethernet Carrier sense multiple access with collision detection-t használ (CSMA/CD – vivő érzékeléses többszörös hozzáférés, ütközés detektálással)., mely egy véletlen közeg hozzáférési protokoll.


## A CSMA/CD bemutatása




**_Carrier Sense (CS):_** A hálózat részét képező végpontok érzékelik, ha egy másik végpont adni kíván a hálózaton.


**_Multiple Access (MA):_** Csak az az állomás veszi figyelembe a csomagot, amelyiknek szól. A többi elutasítja, illetve nem dolgozza fel.

**_Collision Detection (CD):_** Ütközés érzékelése. Ha egyszerre két vagy több eszköz ad a hálózaton, akkor csomagütközés következik be. Ennek elkerülésére a következő procedúrát alkalmazza a szabvány:



	
  1. El kell dönteni, hogy az átküldeni kívánt adat sértetlen-e.

	
  2. Amennyiben az előző pontra a válasz igen, akkor meg kell nézni, hogy a fogadó eszköz nem küld-e éppen.

	
  3. Ha nem, akkor el kell kezdeni a küldést, s közben figyelni kell a hálózatot, nem lesz-e ütközés.

	
  4. Amennyiben ütközés van akkor azt majd lejjebb tárgyaljuk.

	
  5. Az újraküldést jegyző számláló visszaállítása, kerettovábbítás befejezése.


**Ha ütközés történt:**



	
  1. Folytassuk az adatátvitelt, de jelezzük, hogy torzult az adat. Folytassuk ezt mindaddig, míg az összes host észre nem veszi az ütközést.

	
  2. Növeljük meg a számlálót.

	
  3. Elértük a lehetséges újraküldések maximális számát? Szakítsuk meg az átvitelt.

	
  4. Az ütközések számától függően (egy bonyolult matematikai képlet alapján) várjunk, majd folytassuk az elejétől.




## Az Ethernet keret felépítése


[![ethframe](https://armands.blog/images/ethframe.png)](https://armands.blog/images/ethframe.png)

**Előtag**: 7B hosszú, feladata a vevőoldali szinkronizálás.

**SFD**: A keret fejléce, szinkronizációra alkalmas

**Forrás/Célcím:** Küldő/fogadó MAC címe.

**Adat: **max. 1500B

**FCS (CRC): **ellenörzőösszeg


## Kábeltípusok


_Réz:_

A különböző kábel típusok a külső elektromos/mágneses zavarok kivédésére hivatottak.

**UTP:** Szigetelés nélküli, csavart érpárú kábel, mely védett a külső elektromos/mágneses hatásoktól illetve a szomszédos érpárok közti áthallás is megszüntetésre került.
**STP:** Szigetelt és csavart érpárú kábel, melyre az elektromos és mágneses hatások nincsenek hatással.

_Optikai:_

**Egymódusú: **Egy frekvencián képes adatátvitelre, így általában rövidebb távok áthidalására alkalmazzák.

**Többmódusú: **Több frekvencián képes adatátvitelre, így nagyobb távokra alkalmazható,


## Ethernet kábelek típusai


<table align="center">
<tbody>
<tr>

<td width="120" >Kategória
</td>

<td width="120" >Típus
</td>

<td width="120" >Hossz
</td>

<td width="120" >Átviteli sebesség
</td>

<td width="120" >Frekvencia
</td>
</tr>
<tr>

<td width="120" >Cat3
</td>

<td width="120" >UTP
</td>

<td width="120" >100m
</td>

<td width="120" >4Mbps
</td>

<td width="120" >16MJz
</td>
</tr>
<tr>

<td width="120" >Cat4
</td>

<td width="120" >UTP
</td>

<td width="120" >100m
</td>

<td width="120" >16Mbps
</td>

<td width="120" >20MHz
</td>
</tr>
<tr>

<td width="120" >Cat5
</td>

<td width="120" >UTP
</td>

<td width="120" >100m
</td>

<td width="120" >100Mbps
</td>

<td width="120" >100Mz
</td>
</tr>
<tr>

<td width="120" >Cat5e
</td>

<td width="120" >UTP
</td>

<td width="120" >100m
</td>

<td width="120" >1Gbps
</td>

<td width="120" >100Mhz
</td>
</tr>
<tr>

<td width="120" >Cat6
</td>

<td width="120" >UTP
</td>

<td width="120" >100m
</td>

<td width="120" >10Gbps
</td>

<td width="120" >250Mhz
</td>
</tr>
<tr>

<td width="120" >Cat7
</td>

<td width="120" >STP
</td>

<td width="120" >100m
</td>

<td width="120" >10Gbps
</td>

<td width="120" >600MHz
</td>
</tr>
</tbody>
</table>

__Sources:__ [Koax (kép - ELTE)](http://people.inf.elte.hu/reksaai/beadando/pic/koax.gif), [TP (kép - Arcania)](http://www.arcania.hu/Informatika/intro/utp.jpg), [Optikai (kép - szabilinux)](http://www.szabilinux.hu/konya/konyv/2fejezet/Image191.gif), [Cisco Switch (kép)](https://upload.wikimedia.org/wikipedia/commons/7/7f/Cisco_small_business_SG300-28_28-port_Gigabit_Ethernet_rackmount_switch.jpg), [Cisco HUB (kép)](https://w7.pngwing.com/pngs/675/852/png-transparent-wireless-access-points-network-switch-ethernet-hub-cisco-catalyst-port-others-computer-network-electronics-network-switch.png), [Cisco Router (kép)](http://blog.router-switch.com/wp-content/uploads/2011/11/Cisco-1800.jpg), [ISO-OSI-TCP](https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/TCP-IP-ISO-REFERENCE-MODEL-COMPARISON-DIFFERENCE.jpg/800px-TCP-IP-ISO-REFERENCE-MODEL-COMPARISON-DIFFERENCE.jpg), [Ethernet Frame](https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Ethernet_Frame.png/640px-Ethernet_Frame.png)