#Ablakot átméretezünk és lekérdezzük a méreteit. Formázva írjuk ki: a get_window_size könyvtár formában tárolja a
# méreteket, így a formázásban a kulcsra hiatkozunk. A megadot méret (általunk) csak ajánlás, a Chrome dönti el.

#ÚJ FUNKCIÓ: driver.set_window_size(szélesség, magasság), get_window_size




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
    driver.get("http://localhost:9999/responsive-table.html")
    driver.set_window_size(800, 1080)
   # dicti formában adja meg a méretekt, ezeket majd kiírjuk - l. lent (a kulcsra hivatkozunk a szögletes zárójelen
    # belül, míg a kapcsos zárójel a formázást szolgálja)
    size = driver.get_window_size()
    print(f"Window size: width={size['width']}, height={size['height']}")
    time.sleep(2)
    driver.set_window_size(240, 1080)
    print(f"Window size: width={size['width']}, height={size['height']}")
    time.sleep(2)

finally:
    pass