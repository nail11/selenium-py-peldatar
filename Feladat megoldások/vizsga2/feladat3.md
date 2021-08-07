## 3 Feladat: A Harmadik - találós kérdések automatizálása

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a todo app-ot az [https://blue-rock-04e841a03.azurestaticapps.net/harmadik.html](https://blue-rock-04e841a03.azurestaticapps.net/harmadik.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Harmadik app tesztelését.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.

Az alábbiakat tartalmazza a megodásod:
* Helyes válasz ellenőzrése a `Hanyadik feladat ez?` input és button elemkre (pozitív eset elég)
* Titkos jelszó működésének ellenőrzése (pozitív eset elég)
* Számod ki ellenőzrés működése az appban (csak a pozitív vagy egy negatív eset elég)

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `harmadik.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(