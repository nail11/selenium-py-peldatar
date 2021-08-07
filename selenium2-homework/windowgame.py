# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar
# alkalmazást. A program töltse be a példatárból az http://localhost:9999/windowgame.html oldalt.
# A feladatot, hogy megtalád a random kiválasztott színhez tartozó gombot. Ha egy gombra rákattintasz az egy
# új ablakot fog feldobni, egy valamilyen színben tündököl. Ügyelj arra, hogy ne árassza el a képernődet
# a sok ablak.
# A megoldást egy windowgame.py nevű fileban kell beadnod.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import requests

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "http://localhost:9999/windowgame.html"

driver.get(url)
main_window = driver.window_handles[0]
buttons = driver.find_elements_by_tag_name("button")
target_color = driver.find_element_by_id("target_color").text
print("A célablak színkódja: " + target_color)

try:

    for j in range(len(buttons)):
        buttons[j].click()
        #time.sleep(1)
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        new_color = driver.find_element_by_tag_name("h1").text
        if target_color == new_color:
            print("Megvan az ablak ! A színkód: " + new_color)
            break
        else:
            driver.close()
            driver.switch_to.window(main_window)

finally:
   pass #driver.quit()
