
while True:
    eletkor = int(input('Hány éves vagy? :'))

    rendeles = input('Mit kérsz? (sör, kóla) :')

    if rendeles != 'sör' and rendeles != 'kóla':
        print('Csak sorrel es kolaval szolgalhatok.')
        exit()

    if eletkor < 18 and rendeles == 'sör':
        print('Sajnos nem adhatok!')
    elif eletkor >= 60 and rendeles == 'kóla':
        print('Sajnos nem adhatok, mert megemeli a vernyomasod!')
    else:
        print(f'parancsoljon itt a {rendeles}')