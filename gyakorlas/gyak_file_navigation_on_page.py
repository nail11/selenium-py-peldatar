# environment settings
#......................................................................
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
# from selenium.webdriver.common.keys import Keys
# from datetime import date
import time
# from pathlib import Path
# import pprint

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# In order for ChromeDriverManager to work you must pip install it in your own environment.

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "http://localhost:9999/"

def navigate_to_page(page_name):
    page = driver.find_element_by_xpath(f"//a[text()='{page_name}']")
    page.click()

try:
    driver.get(url)
    # mindkét következő  megoldás jó
    #general_text = driver.find_element_by_xpath("//a[text()='General text and other elements']")
    #general_text = driver.find_element_by_xpath("//a[@href='general.html']")

    # de a fenti függvényt hívjuk inkább
    # hogy lássuk, hogyan mozgunk, kiíratjuk az url-eket

    print(driver.current_url)
    navigate_to_page("General text and other elements")
    print(driver.current_url)
    #time.sleep(1)    - ha kiíratjuk az url-t akkor nem kell szemmel ellenőrizni, nem kell megállni
    driver.back()
    print(driver.current_url)
    #time.sleep(1)
    navigate_to_page("General text and other elements")

# a lap tetején a különbözö anchor elemekre kattintva mozgunk a lapon belül

    anchors = driver.find_elements_by_xpath("//header//small//a")

    for a in anchors:
        a.click()

# kiíratjuk az url, ami az adott szekcióhoz tartozik (szerencsére ezeknek külön url-je van)

        print(driver.current_url)




finally:
    pass