# Ha egy ablakba egy másikból szeretnénk információt másolni, akkor a következőt tesszük:
# Elmentjük a fogadó ablakot - driver.window_handles[] (a nulladik ablak az, amiben állunk)
# Java script futtatásával megnyitunk egy másik ablakot: driver.execute_script() és elmentjük a window_handles-be
# a switch_to_window függvénnyel átváltunk az új ablakba
# ebben megnyitjuk a general.html-t
# kikeresünk egy mezőt, aminek a tartalmát az eredeti ablak (oldal) valamelyik mezejébe írunk, és elmentjuk egy változóbe
# visszakapcsolunk az eredeti ablakra és kikeressük a célmezőt és rrlküldjük bele a változó tartalmát (a send_keys()
# úgy működik, hogy meg kell előtte adni mibe küldjük  - valami.send_keys(valami)
# ha mindkét ablakot be akarjuk zárni, akkor a driver.quit()-tel zárunk (a driver.close() csak az aktuális ablakot zárja)


#ÚJ KIFEJEZÉSEK: window_handles[], driver.quit()



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
    driver.get("http://localhost:9999/forms.html")
    main_window = driver.window_handles[0]
    #Java script futtatása - windows.open - a második paraméter a neve az ablaknak
    driver.execute_script("window.open('', 'newwin', 'height=800,width=600')")
    new_window = driver.window_handles[1]
    #átlép az  új ablakba és megnyit egy url-t, Ez a Java függvény paramétere is lehetne
    driver.switch_to.window(new_window)
    driver.get("http://localhost:9999/general.html")
    # ezen a tag neme -on csak egy elem van
    text = driver.find_element_by_tag_name("h4").text
    driver.switch_to.window(main_window)
    example_input = driver.find_element_by_id("example-input-text")
    example_input.send_keys(text)
    time.sleep(1)

finally:
    pass #driver.quit()