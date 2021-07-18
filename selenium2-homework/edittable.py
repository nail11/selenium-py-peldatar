# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a
# selenium-py-peldatar alkalmazást. A program töltse be a példatárból az http://localhost:9999/editable-table.html
# oldalt. A megjelenő táblázatban az alábbi feladatokat kell végrehajtanod: a) Addj hozzá még két teljsen
# kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok. b) Ellenőrizd a kereső funkciót.
# c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.
# A megoldást egy edittable.py nevű fileban kell beadnod.

from selenium import webdriver
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()

driver.get("http://localhost:9999/editable-table.html")


# megtalál egy elemet path alapján és törli a tartalmát, ha az container
def find_element_by_path(path):
    element = driver.find_element_by_xpath(path)
    # element.clear()
    return element


# megtalálja  azt a gompot a path alapján amivel egy táblázathoz további sorokat lehet adni,
# és n számú üres sort ad hozzá
def add_button_click(path, n):
    add_button = driver.find_element_by_xpath(path)
    for n in range(n):
        add_button.click()


# egy tábla adott sorára ugrik
# def jump_to_row(table_name, r):
# for r in range(r):
# next(table_name)


with open('table_datas.csv', 'r') as t:
    t_datas = csv.reader(t, delimiter=',')

    next(t_datas)

    add_button_click('//*[@id="container"]/div/div[2]/button', 2)


    for row in t_datas:
        rows_in_table = driver.find_elements_by_tag_name('tr')
        empty_rows = rows_in_table[7:9]
        for r in empty_rows:
            cells = r.find_elements_by_tag_name('td')
            for i, cell in enumerate(cells):
                print(i)
                print(type(cells[i]))
                print(cells[i])
                #cell.click()
