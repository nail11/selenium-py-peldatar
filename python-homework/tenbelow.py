x = 0
y = 0
while x<10:
    x = int(input('Adj meg egy számot: '))
    if x < 10:
       y += x
print('Az eddig megadott 10-nél kissebb számok összege: '+ str(y))
