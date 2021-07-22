# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar
# alkalmazást. A program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt.
# Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
# A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük, hogy hanyadiknak lett
# megjelenítve és cat_id meg az azonosító amit szolgáltató ad. A {} jelek ne legyenek benne a fájlnévben.
# A megoldást egy catloader.py nevű fileban kell beadnod.

# ÚJ KÖNYVTÁR: os
# új dolgok: új könyvtár készítése, text fájl feltöltése ciklusból

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "http://localhost:9999/loadmore.html"

try:
    driver.get(url)
    cat_list = []
    os.makedirs('./catdir')
    load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")
    for i in range(3):
        load_more.click()
        time.sleep(3)
        images = driver.find_elements_by_xpath("//div[@class='image']")

    for k, j in enumerate(images[0:20]):
        cat_id = (f'{k + 1}_{(j.find_element_by_tag_name("p").text)[8:]}')
        with open("./catdir/cat_ids.text", "a") as c_list:
            c_list.write(cat_id + ",\n")

finally:
    driver.close()
