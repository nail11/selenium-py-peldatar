# Teljes javascript kódot szövegként adunk meg, és driver.execute_sript() utasítással végrehajtatunk
# a böngészővel. Az alert() függvény egy alert ablakot ad a böngészőre

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pprint

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999")

    js = "alert('Hello World!');"
    driver.execute_script(js)


finally:
  driver.close()