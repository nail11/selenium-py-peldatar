import csv

with open('elso_csv.csv') as csvfile:

    for sor in csv.reader(csvfile, delimiter=','):
        print(sor)
print('---')
with open('elso_csv.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(type(csvreader))
    next(csvreader)
    for sor in csvreader:
        print(sor)