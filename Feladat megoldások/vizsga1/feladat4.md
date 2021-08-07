#4. Feladat: Productum

Adott egy nem üres `numbers` mevű lista Pythonban:
```Python
# for example
numbers = [1, 2, 3, 4]
```

A lista legalább 2 számot tartalmazzon. Nincs felső korlát arra, hogy maximúm hány számot tartalmazhat.

írj egy Python programot ami össze szorozza a `numbers` lista elemeit és kiírja az eredményt. Vegyél fel magadnak egy teszt listát és arra írd meg a műveleteket. A programod ne csak kiírja a szorzás eredményét (beégetett konstans szövegként), hanem tényleg végezze el a műveletet.

A fenti példára a következő eredménynek kell kiíródnia:
```
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
```

Ügyelj arra, hogy a kiírás pontosan kövesse a fenti példa mintáját, azaz:
```
{eredeti lista tartalma} => {a szorás képlete} => {a művelet eredménye}
```

### Tanácsok a megoldáshoz:
* Nem kell ellenőrizned, hogy a listában csak számok vannak-e
* Nem kell ellenőrizned, hogy a lista tartalmaz-e legalább 2 számot
* Nem kell ellenőrizned, hogy csak pozitív számokat tartalmaz-e a lista
* A fentihez hasonló egyszerű listával teszteld a kódod, ami értelmes a feladatra és ami egyértelmű választ ad
* Nincs pontlevonás ha `lehetne ezt egyszerűbben is`
* Nincs plusz pont ha `kevesebb sorból oldod meg`, (a feladatnak van pár soros, egy soros és sok soros megoldása is, mind játszik és mindre lehet sok részpontot adni)


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `productum.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(