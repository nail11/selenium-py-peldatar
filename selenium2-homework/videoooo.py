# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar
# alkalmazást. A program töltse be a példatárból az http://localhost:9999/videos.html oldalt. Az oldalon
# találhotó összes beágyazott videót indítsa el és állítsa meg.
# A megoldást egy videoooo.py nevű fileban kell beadnod.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pathlib import  Path
import pprint


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "http://localhost:9999/videos.html"

try:
    driver.get(url)

    frame_names = driver.find_elements_by_tag_name("h3")

    frame1 = driver.find_element_by_id("html5video")
    frame2 = driver.find_elements_by_id("video1")
    click_but =driver.find_elements_by_tag_name("button")[0]
    frame3 = driver.find_element_by_id("youtubeframe")

    on_clicks = [frame1, click_but, frame3]

    def video_start_stop(click, name):

        for i, click in enumerate(on_clicks):
            on_clicks[i].screenshot('screenshot1.png')
            scr_shot1 = Path('screenshot1.png').stat().st_size
            on_clicks[i].click()
            time.sleep(5)
            scr_shot2 = Path('screenshot2.png').stat().st_size
            on_clicks[i].click()

            assert scr_shot1 != scr_shot2
            print(f"A két screenshot nem azonos, '{frame_names[i].text}' elindult és megállt!")

    video_start_stop(on_clicks,frame_names)

finally:
    driver.close()