# 2. Feladat: Imperial-Metric konverzió

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be az mértékegység konvertáló app-ot az [https://proud-cliff-00bebe803.azurestaticapps.net/masodik.html](https://proud-cliff-00bebe803.azurestaticapps.net/masodik.html) oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a converterben:

### TC_001: 
* Bevitel: 
    * <első beviteli mező>: `112`
    * <masodik beviteli mező>: `meter`
* Elvárt eredmény: 
    * <harmadik mező>: `367.45406824146977 FOOT`

### TC_002: 
* Bevitel: 
    * <első beviteli mező>: `8`
    * <masodik beviteli mező>: `oz`
* Elvárt eredmény: 
    * <harmadik mező>: `236.56 MILLILITER`

### TC_003: 
* Bevitel: 
    * <első beviteli mező>: `1`
    * <masodik beviteli mező>: `gallon`
* Elvárt eredmény: 
    * <harmadik mező>: `30.28 LITER`

## Ne gondold túl a dolgot :)

* Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
* Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
* Nem kell a kezdeti megjelenést tesztelned, tételezzük fel, hogy ez már tesztelve van egy másik teszt esetttel

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket selektorokkal, megint jár a pont érte
* megnyomjuk egy gombot, ismét pont jár érte
* ellenőrizz `assert` vagy `if-else` struktúra és `print` függvény segítségével, megintcsak jár a pont 

## A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `masodik.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* bármilyen kódot is adsz be arra ügyelj, hogy a Pycharm ne húzza alá pirossal a kódodat, mert az szintaktikailag helyetelen kódot eredményez. Ilyenkor vagy javítsd ki a szintaktikai hibákat, vagy kommenteld ki a kódsorokat.
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(