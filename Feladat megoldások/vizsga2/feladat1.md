## 1 Feladat: Kalkulátor automatizálása

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a kalkulátor app-ot az [https://blue-rock-04e841a03.azurestaticapps.net/elso.html](https://blue-rock-04e841a03.azurestaticapps.net/elso.html) oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a kalkulátorban:

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.

Összeadás művelet helyessége:
    1 + 99 == 100 
    -5 + 5 == 0

Törlés gomb helye működése:
    1 + 2 == 3 C --> 0
    1 + C --> 0

Százalék számítás helyes működése:
    99 + % == 0.99

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `elso.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(