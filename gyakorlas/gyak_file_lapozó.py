# lapozható táblákban kihasználhatjuk, hogy az elöre, hátra lapozást nyilak teszik lehetővé,
# így végig mehetünk a táblákon

#az xPath így ahogy volt kimásolható

# a sorokat a táblán belül lehet keresni (rows = table.find_elements......), és a cellákat a sorokban
# (cells = row.find_elements_....) Az adatokat itt szótár típusban tároljuk az adatokat (kulcs:érték)
# - jó példa a szótár használatra

# vizsgáljuk a next gomb (utolsó gomb, id=next) állapotát, ha az utolsó lapon vagyunk, akkor disabled
# (valami.is_enabled vagy valami.is_disabled)

# while True - egy vgtelen ciklust b generál, amiből a break-el törünk ki, ha next gomb not enabled

# KIFEJEZÉSEK: pprint.pprint(), valami.is_enabled
import pprint

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
driver = webdriver.Chrome()

extracted_data = []

try:
    driver.get("http://localhost:9999/pagination.html")
    while True:
        table = driver.find_element_by_xpath("//table[@id='contacts-table']/tbody")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text
            extracted_data.append(data_row)
        next_button = driver.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()
    pprint.pprint(extracted_data)
    print(len(extracted_data))
finally:
    driver.close()