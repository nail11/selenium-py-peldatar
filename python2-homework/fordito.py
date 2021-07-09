# egész számokat kér be, míg 0-t nem kap, majd kiírja fordított sorrendben

def num_turn():
    x = 1
    list = []

    # x = int(input('Adj meg egy nullától küklönböző egész számot: '))

    # if isinstance(x, (int)):

    while int(x) > 0:
        x = input('Adj meg egy nullától küklönböző egész számot: ')

        if int(x) > 0:

            list.append(x)

        elif int(x) == 0:

            print('A megadott szám 0, befejezem a számok bekérését !')

            print('A számlista: ')

            print(list)

            print('A fordított számlista:')

            print(list[::-1])


# a fordító függvény meghívása

num_turn()
