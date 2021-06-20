print()
print("Számold-ki az utazásod benzinköltségét!")
print()

a = input("Fogyasztás országúton (l/100 km) ?: ")
b = input("Fogyasztás városban (l/100 km) ?: ")
c = input("Országúton megtett út (km) ?: ")
d = input("Városban megtett út (km) ?: ")
e = input("Benzin ára? (Ft/l): ")
f = input("Vissza is térsz ezen az úton (igen=i/nem=n)? ")

koltseg=(((int(a)*int(c))+(int(b)*int(d)))*int(e))/100

if f == "n":
    print("Ezekkel az adatokkal a benzinköltség: "+str(koltseg) +"  Ft")
elif f == "i":
    print("Ezekkel az adatokkal a benzinköltség: "+str(2*koltseg) +"  Ft")
else:
    print("A válasz értelmezhetetlen!")