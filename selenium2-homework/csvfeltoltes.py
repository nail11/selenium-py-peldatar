#Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan
# a selenium-py-peldatar alkalmazást. A program töltse be a példatárból az
# http://localhost:9999/another_form.html oldalt. A program segítségével olvassd be a csv tartalmat.
# A feladatod, hogy az oldalon található formanyomtatvány segítségével feltöltsd a táblázatot.
# Használd a Python CSV könyvtárát. A feltöltött táblázatot ellenőrizheted ha a probramod letölti a táblázat
# alatti gomb segítségével az aktuális tartalmat. Hasonlítsd össze python kódból a kapott file-t,
# hogy identikus-e az eredetivel.

import csv

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()

driver.get("http://localhost:9999/another_form.html")

def find_element_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


with open('table_in2.csv', 'r') as csvin:
    csv_in = csv.reader(csvin, delimiter=',')
    print(type(csv_in))
    next(csv_in)
    for row in csv_in:
        print(row)
        find_element_by_id('fullname').send_keys(row[0])
        find_element_by_id('email').send_keys(row[1])
        find_element_by_id('dob').send_keys(row[2])
        find_element_by_id('phone').send_keys(row[3])
        driver.find_element_by_id('submit').click()