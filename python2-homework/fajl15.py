# Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy, hogy nem tárolod el a szöveget,
# hanem minden sort azonnal kiírsz!
# A megoldást egy fajl5.py nevű file-ban kell beadnod.

with open('adat.txt', 'r') as f:
    txt = f.read()
    text_proc = txt.split()

# text_proc egy lista
# az adat.txt tartalmának kiírása adat2.txt-be, közben soronként kiírom a szöveget

with open('adat2.txt', 'w') as f1:
    for i in text_proc:
        print(i)
        f1.write(i +'\n')

# adat2.txt fájlban szerepel soronként

