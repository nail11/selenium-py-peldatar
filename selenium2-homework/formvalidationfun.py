#Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar
# alkalmazást. A program töltse be a példatárból az http://localhost:9999/simplevalidation.html oldalt.
# A tanultak alapján teszteld le az űlap mező ellőnőrző funkcióit.
#A megoldást egy formvalidationfun.py nevű fileban kell beadnod.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pprint


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/simplevalidation.html")


finally:
    pass