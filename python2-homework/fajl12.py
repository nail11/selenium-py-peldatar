# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!
# A megoldást egy fajl2.py nevű file-ban kell beadnod.

with open('adat.txt', 'r') as f:
     txt = f.read()
     text_proc = txt.split()

# text_proc a lista

     print(*text_proc)