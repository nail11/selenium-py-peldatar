# vidomanipulálása nehéz, mert a gyártók igyekeznek ezt lehetetlenné tenni. Egér akciókat nehÉz
# szimulálni (vagy most nem akarjuk),
# így a billentyüket használjuk - ehhez importálni kell  kEYS OSZTÁLYT
# azt, hogy egy video elindult-e, legegyszerübben úgy tudjuk ellenőrizni, hogy egy screenshot-ot készítünk


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import time

driver = webdriver.Chrome()

try:

    driver.get("http://localhost:9999/videos.html")

    html5video = driver.find_element_by_id("html5video")
    html5video.click()
    html5video.send_keys(Keys.SPACE)
    time.sleep(5)
    html5video.screenshot('video_screenshot.png')

finally:
   driver.close()