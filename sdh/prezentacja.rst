----

:data-x: 300
:data-y: 2000

Technologie sieci transportu informacji
=======================================

SDH vs PDH

----

:data-x: r1500
:data-y: r1500


Plesiochronus Digital Hierarchy
===============================

| Plezjochroniczna -> *plesio* - prawie, *chrono* - czas.
| Oznacza to że elementy sieci *PDH* są ze sobą zsynchronizowane,
  ale nie idealnie, gdyż każdy z elementów sieci posiada swój zegar.
| *PDH* używa *TDM*

----

:data-x: r500
:data-y: r500
:data-rotate: 90
:data-scale: 0.1

Wspiera:
--------

  - *cyfrowe* kanały głosowe z szybkością transmisji *64kbps*,
  - *no store and forward*


----

:data-x: r500
:data-y: r500
:data-scale: 1


Multipleksacja w PDH
--------------------

By przenieść *2Mbps* danych z jednego punktu do drugiego, owe strumienie danych są
multipleksowane w grupy bitow, które zawierają po jednym bicie z każdego strumienia.
Jest też dodawany dodatkowy bit -> *bit stuffing* który pozwala zdekodować z którego
strumienia danych bit pochodzi.

----

:data-x: r1500
:data-y: r1500
:data-z: 4000
:data-scale: 3

Synchonizacja w PDH
-------------------
| W *PDH* każde urządzenie ma swój zegar przez co synchronizacja sieci jest niemożliwa.
  Z pomocą przychodzi *FAW* Frame Alignment Word.

----

:data-x: r0
:data-y: r4000

Ograniczenia PDH
----------------


- nie jest elastyczne, podłaczenie do innych sieci jest bardzo kosztowne i trudne
- brak możlowości monitorowania performensu, przez co cięzko zoptymalizować sieć
- brak standardów , PDH ma rózne hierarchie multipleksowania, i cieżko
  zintegrować wszystkie sieci
- PDH nie pasuje idealnie do połączeń o dużych przepustowościach
- kiedy przychodzi strumien o niższej przepustowości , cały system musi
  ulec demultipleksacji
- maksymalna pojemność wynosi 566Mps
- PDH pozwala tylko na konfiguracje poin-2-point


----

:data-x: r0
:data-y: r4000

Hierarchia w PDH
----------------

.. image:: pdhTable.png
  :height: 500
  :width: 700 px
  :scale: 50 %
  :alt: alternate text
  :align: center

----

:data-x: r470
:data-y: r950
:data-scale: 0.08

SDH - Synchronous Digital Hierarchy
===================================
  | W przeciwnieństwie do PDH, SDH jest oparte na powtarzającej się hierarchii ramek
    o stałej długości
  | Eliminuje bardzo dużo zbędnej multipleksacji.


----

:data-x: r0
:data-y: r180

Najbardziej popularne szybkosci dla SONET/SDH
---------------------------------------------

.. image:: sdhTable.png
  :height: 500
  :width: 700 px
  :scale: 50 %
  :alt: alternate text
  :align: center

----

:data-x: r20
:data-y: r180
:rotare: 130


W skład SDH wchodzi:
--------------------

- Synchronous mutiplexer
- Synchronous Digital Cross Connect
- Regenerators


----

:data-x: r20
:data-y: r180

Struktura ramki
---------------

  | Struktura ramki jest oparta na synchronicznej bitowej multipleksacji kilku bloków.
  | Podstawową ramką transmisyjną jest STM-1 (Synchronous Transport Module).
  | Ramka trwa 125 micro sec, i jest to równoznaczne z *0.125kHz*.

----

:data-x: r1500
:data-y: r1500
:data-rotate: -90
:data-scale: 3

Zalety SDH
----------
  - W porównaniu do PDH, SDH szybkość transferu może być nawet do 10Gbps.
  - Auto repair and backups.
  - Jest dużo mniej skomplikowany niż PDH.
  - Jest kompatybilny z PDH.



----

:data-x: r2220
:data-y: r1280

Dziękuję
========
