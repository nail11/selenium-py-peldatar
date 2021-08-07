#csak HTML!-ben müködik igazán, HTML5 ben csak az un. dragable elemek vonszolhatók kijelölt konténerekbe, és ehhez is
# csak megkerülő megoldások vannak

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pprint


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())


try:
    driver.get("http://localhost:9999/dragndrop1.html")

    # JAVASript kell
finally:
    pass