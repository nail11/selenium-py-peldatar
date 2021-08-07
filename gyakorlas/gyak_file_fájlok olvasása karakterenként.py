with open("gyak.txt", "r") as f:
    res = f.read(6)

    # a zárójelek között álló szám azt mondja meg, hány karaktert akarok
    # - ez most 6. így amit kiír = három (ez 5) plusz a sortörés

    print(res)

    # lehet folytatni tovább - a következő 5 karakter = négy,

    res2 = f.read(5)
    print(res2)