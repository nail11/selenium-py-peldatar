# anchor link = hashmark-al (#) jelölt belső link, a honlapon belülre mutat - id tag-eel rendelkező szekcióra ugrik
# másik lehetőség: kiveszem az ős (egyetlen van csak belőle) tag-et, a html-t. Ez az egész lapot lefedi és lehet END
# vagy egyéb irányt megadni a send_keys() utasítással (+ Keys.valami)
# még egy lehetőség: javascript - driver.execute_script(js)

#ÚJ KIFEJEZÉSEK: execute_script()


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pprint

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/general.html")


# anchor keys
    
    # oldalon belül aznanchore link-re kattintatva

# Keys
    #html = driver.find_element_by_tag_name("html")

    # html tag az őstag, mindíg 1 van belőle, és a látható képernyőn kívüli tarülatakat is kijelöli

    #time.sleep(1)
    #html.send_keys(Keys.END)
    #time.sleep(1)

# Javascript

    js = "window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(js)
    time.sleep(2)



finally:
    driver.close()