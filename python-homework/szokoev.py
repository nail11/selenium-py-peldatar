

def szokoev(ev):
    if (ev % 100 == 0):
        if (ev % 4 == 0) or (ev % 400 == 0):
            return 'Igaz'
        else:
           return 'Hamis'
    else:
     return 'Hamis'

ev = int(input('Melyik évről akarod eldönteni, hogy szökőév-e? '))

print(szokoev(ev))
