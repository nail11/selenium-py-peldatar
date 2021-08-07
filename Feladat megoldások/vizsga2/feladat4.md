## 4 Feladat: Számfordító

Készíts egy Python python applikációt (egy darab python file) ami megfordítja a számjegyeket egy nagy számban.

```Python
# - You have to write an application where a user gives you non-negative integer, and you have to convert it to a list 
#   and reverse that list.
number = "123456789" 
reverted_number = rev_num(number) # should work only for non negative numbers
print(reverted_number)
# 987654321
```

További tesztadatok és eredmények:
```Python
number = "86652" 
reverted_number = rev_num(number) # should work only for non negative numbers
print(reverted_number)
# 25668
```
```Python
number = "1" 
reverted_number = rev_num(number) # should work only for non negative numbers
print(reverted_number)
# 1
```
```Python
number = "11" 
reverted_number = rev_num(number) # should work only for non negative numbers
print(reverted_number)
# 11
```
### Tanácsok a megoldáshoz:
* Fontos, hogy függvényt adjál be
* Fontos, hogy ne triviális megoldást adj be (a felnti számokra működik csak de ha egy másik tesztadattal próbáljuk arra nem műküdik)
* Ne gondold túl!
* Bérmilyen megodás ami a fenti teszt adatokra (és hasonló tesztadatokra) a helyes megoldást adja tökéletesen megfelel
* Nincs pontlevonás ha `lehetne ezt egyszerűbben is`
* Nincs plusz pont ha `kevesebb sorból oldod meg`


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `rev_num.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(