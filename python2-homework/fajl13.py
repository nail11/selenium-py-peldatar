# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként egy másik fájlba!
# A megoldást egy fajl3.py nevű file-ban kell beadnod.

with open('adat.txt', 'r') as f:
    txt = f.read()
    text_proc = txt.split()

# text_proc egy lista

with open('adat2.txt', 'w') as f1:
    for i in text_proc:
        f1.write(i +' ')

# a szöveg adat2.txt fájlban szerepel egy sorban


