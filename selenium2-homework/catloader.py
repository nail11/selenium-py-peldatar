# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar
# alkalmazást. A program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt.
# Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
# A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük, hogy hanyadiknak lett
# megjelenítve és cat_id meg az azonosító amit szolgáltató ad. A {} jelek ne legyenek benne a fájlnévben.
# A megoldást egy catloader.py nevű fileban kell beadnod.

# ÚJ KÖNYVTÁR: os, request
# új dolgok: új könyvtár készítése és ellenőrzáse, hogy megven-e, request HTML-hez, féjl letöltése egy
# adott néven elmentése (.content)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import requests

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "http://localhost:9999/loadmore.html"

try:
    driver.get(url)
    if not os.path.isdir('./catdir'):
        os.makedirs('./catdir')
    load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")
    for i in range(3):
        load_more.click()
        time.sleep(3)
        images = driver.find_elements_by_xpath("//div[@class='image']")

    for k in range(len(images)):
        image_url = images[k].find_element_by_tag_name("img").get_attribute("src")

        print(image_url)
        real_image = requests.get(image_url)
        cat_id = (f'./catdir/{k + 1}_{(images[k].find_element_by_tag_name("p").text)[8:]}')
        cat_image = f"{cat_id}.{image_url[-3:]}"
        with open(cat_image, "wb") as ima:
            ima.write(real_image.content)

finally:
    driver.close()
