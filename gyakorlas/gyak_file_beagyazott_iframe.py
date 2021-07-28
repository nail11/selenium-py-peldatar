# Az IFrame-k úgy müködnek, mint önálló ablakok, csak a főablak html-en belül van egy másik html. Itt az egyik
# IFrame-ből adatot másolun a másikba. Itt nem window_handles-t használunk az ablakok közötti váltásra,
# hanem elementeket. A switch_to metódust használjuk, de a driver csak alá-fölé rendeltségi vszonyban tud váltogatni, és
# ezek az ablakok nem ilyan viszonyban vannak, így előbb a szülő ablakra kell váltani

#ÚJ FUNKCIÓ: switch_to.frame,  parent_frame



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
    driver.get("http://localhost:9999/embeds.html")

    general_frame = driver.find_element_by_id("general-frame")
    forms_frame = driver.find_element_by_id("forms-frame")

    driver.switch_to.frame(general_frame)
    h4text = driver.find_element_by_tag_name("h4").text

    #a váltáshoz előbb a szülő ablakra kell váltani
    driver.switch_to.parent_frame()

    driver.switch_to.frame(forms_frame)
    driver.find_element_by_id("example-input-text").send_keys(h4text)
    time.sleep(2)


finally:
    driver.close()