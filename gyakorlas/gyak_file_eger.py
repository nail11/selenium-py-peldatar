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
    driver.get("http://localhost:9999/kitchensink.html")

    mousehover = driver.find_element_by_id("mousehover")

    # keresünk egy olyan div-et aminek a class-a alább látható és ennek is az a[1]-ét
    top_hover = driver.find_element_by_xpath("//div[@class='mouse-hover-content']/a[1]")

    #erre fogalmazunk egy akciót az AcionChain-nel, de előbb meg kell jeleníteni - rávisszük az egeret
    # lepéldányosítjuk az ActionChains-t, ez lesz az "actions"
    actions =ActionChains(driver)

    # most jönnek az akciók
    actions.move_to_element(mousehover)  #ez a builder pattern
    actions.click(top_hover)

    #a végrehajtás akkor jön, amikor úgy gondolom
    actions.perform()

    #lehet ezt szétszedni és máa fomában is pl.

    ActionChains(driver).move_to_element(mousehover).perform()
    time.sleep(1)
    ActionChains(driver).click(top_hover).perform()


finally:
    pass