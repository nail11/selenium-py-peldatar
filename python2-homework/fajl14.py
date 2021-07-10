# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így, ahogy beolvastad, soronként
# egy szóval egy másik fájlba!
# A megoldást egy fajl4.py nevű file-ban kell beadnod.

with open('adat.txt', 'r') as f:
    txt = f.read()
    text_proc = txt.split()

# text_proc egy lista

with open('adat2.txt', 'w') as f1:
    for i in text_proc:
        f1.write(i +'\n')
with open('adat2.txt', 'r') as f2:

# adat2.txt fájlban szerepel soronként

        print(f2.read())