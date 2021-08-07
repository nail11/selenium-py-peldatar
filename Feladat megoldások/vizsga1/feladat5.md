# 5. Feladat: Sepcial 11

Nevezzük speciálisnak azokat a számokat, amik `11` többszörösei (másként fogalmazva oszthatók `11`-el) vagy pont `1`-el nagyobbak mint `11` valamelyik többszöröse (másként fogalmazva `x-1` már osztható `11`-el).

írj egy olyan Python függvényt, ami megkapja a tesztelt számot paraméterként és visszaadja, hogy a kérdéses szám az speciális vagy nem:

```Python
special_eleven(22) -> True
special_eleven(23) -> True
special_eleven(24) -> False
```

Próbáld ki a függvényed az alábbi számokra:
```
23, 24, 122, 96
```

### Tanácsok a megoldáshoz:
* Nem kell ellenőrizned, hogy a egész számot kaptál-e a függvény bemenő paramétereként
* Nincs pontlevonás ha `lehetne ezt egyszerűbben is`
* Nincs plusz pont ha `kevesebb sorból oldod meg`
* Mindenképpen függvényt addj be kérlek, mert az is pontot ér, mivel ez a feladat.

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `productum.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(