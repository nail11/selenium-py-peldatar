kor = input('Hány éves vagy ? ')
ital = input('Mi a válsztott italod, sör vagy kóla ? ')

if ital == 'kóla':
    if int(kor) >= 60:
        print('A kóla emeli a vérnyomást!')
    else:
        print('Parancsolj, a kólád! Egészségedre!')
elif ital == 'sör':
    if int(kor) < 18:
        print('Kiskorú vagy, nem adhatök sört!')
    else:
        print('Paroncsolj, a söröd! Egészségedre!')
else:
    print('Ilyen ital nincs nálunk! Csak sört, vagy kólát választhatsz!')
