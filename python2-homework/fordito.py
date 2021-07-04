# egész számokat kér be, míg 0-t nem kap, majd kiírja fordított sorrendben

def num_add():
    x = 1
    list = []
    while x > 0:

        x = int(input('Adj meg egy egész számot: '))
        if x > 0:

            list.append(x)

        else:

            print('A megadott szám 0, befejezem a számok bekérését !')

            print('A számlista: ')
            print(list)

            print('A fordított számlista:')

            print(list[::-1])

    return

# a fordító függvény meghívása

num_add()



