def special_eleven(num):
    #  számok vizsgálata maradékos osztással, hogy 11-el oszthatóak e
    if num % 11 == 0:
        return True
    elif (num - 1) % 11 == 0:  # megvizsgáljuk, hogy a kapott számból ha kivonunk egyet, akkor osztható el 11-el
        return True
    else:
        return False


if __name__ == "__main__":
    # függvény tesztelése megadott tesztadatokkal ciklusban
    test_data = [23, 24, 122, 96]
    for n in test_data:
        print(f'{n} is special?: {special_eleven(n)}')
