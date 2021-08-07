# 3. Feladat: Őrült pénzfeldobás!

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be az mad coinflip app-ot az [https://proud-cliff-00bebe803.azurestaticapps.net/harmadik.html](https://proud-cliff-00bebe803.azurestaticapps.net/harmadik.html) oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat az appban:

### TC_000: Kezdeti értékek
* Elvárt eredmény: 
    * Money: `100`
    * Bet: `<üres>`
    * Result: `-`

### TC_001: 
* Bevitel: 
    * Bet: `10`
    * Nyomjuk meg a `Tails` feliratú gombot
* Elvárt eredmény: 
    * Result: `heads` vagy `tails`
    * ha eltaláltuk:
        * Money: `110`
    * ha nem találtuk el:
        * Money: `90`

## Ne gondold túl a dolgot :)

* Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
* Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket selektorokkal, megint jár a pont érte
* megnyomjuk egy gombot, ismét pont jár érte
* ellenőrizz `assert` vagy `if-else` struktúra és `print` függvény segítségével, megintcsak jár a pont 

## A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `harmadik.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* bármilyen kódot is adsz be arra ügyelj, hogy a Pycharm ne húzza alá pirossal a kódodat, mert az szintaktikailag helyetelen kódot eredményez. Ilyenkor vagy javítsd ki a szintaktikai hibákat, vagy kommenteld ki a kódsorokat.
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(