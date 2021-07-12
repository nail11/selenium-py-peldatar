# Készíts egy python programot ami a fenti adatfileból készít egy másik adatfájl-t ami
# csak az emailím és név oszlopokat tartalmazza. Tehát például:
# Email,Name
# peter.kiss@sel.hu,Kiss Péter
# ervin.nagy@sel.hu,Nagy Ervin
# ...
# A megoldást egy `csvszures.py` nevű fileban kell beadnod.
import csv

with open('table_in.csv', 'r') as csvin, open('table_out.csv', 'w') as csvout:
    csv_in = csv.reader(csvin, delimiter=',')
    for row in csv_in:
        csvout.write(row[1] + ',' + row[3] + '\n')
        # print(row[1]+','+row[3])
