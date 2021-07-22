# elsőként megkeressük a loadmoe gombot és betöltjük a load_more változóba

# megkeressük a képeket - listát kapunk
# iterálunk a lista elemein és megkeressük (majd kinyomtatjuk) a képek jellemzőir
# meghívjuk click()-el 5x

# beágyazott ciklusban az előzőleg kiszedett elemeken iterálunk !: "images"-t megkerestük, ez listát adott és ezen
# iterálunk végig, hogy az egyes elemek ("j" a lista elemei lesznek (végig megy az egész "images" listán és visszaadja
# a "j" elemeket mind).


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pprint

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/loadmore.html")
    load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")
    for i in range(5):
        time.sleep(3)
        images = driver.find_elements_by_xpath("//div[@class='image']")
        for j in images[-5:]:
            print(j.find_element_by_tag_name("img").get_attribute("src"))
            print(j.find_element_by_tag_name("p").text)
        load_more.click()

finally:
    pass #driver.close()
