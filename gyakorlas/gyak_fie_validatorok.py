# CRTL CLICK egy néven (pl, függvény) - behozza a leírást
#
# beépített validétorok használata - pl, megfelelö formétum stb.

# vérakozés beállításe a WebDriverWait funkcióval (osztály) - ehhez be kell importálni

# hogy meddig várakozzék, ahhoz megkell adni egy feltételt . ezek az EC könyvtárban vannak ehhez megint importálni kell
# egy könyvtárt - ez az expected_conditions amire mint EC hvatkozunk (ahogy elkezdjük beírni a from....import formulát
# a pontok után megjelennek a lehetőségek

# lokátor új formája - By (ehhez is kell könyvtár). A szögletes zárójelen belül lehet komplett logikai kifajazés

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver
import time

driver = webdriver.Chrome()

try:

    driver.get("http://localhost:9999/another_form.html")

    driver.find_element_by_id("submit").click()

    msg = WebDriverWait(driver, 2).until(
        # megadjuk a feltételt - várunk (max.20 másodper) addig, amíg a "validationMessage" meg nem jelenik. Az utasítás
        # kiolvassa az üzenetet és ezt elmentjük msg változóba
        EC.visibility_of_element_located((By.XPATH, "//input[@id='fullname and @name='fullname'']"))).get_attribute(
            "validationMessage")

    # megvizsgáljuk, hogy van-e validásciós üzenet

    assert msg is not None
    assert msg == "Kérjük, töltse ki ezt a mezőt."

    time.sleep(2)

finally:
    pass
