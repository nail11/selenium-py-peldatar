import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/trickyelements.html")

for i in range(1, 6):

   #element_list = (driver.find_element_by_id( 'element'+str(i)))

   element = driver.find_element_by_tag_name("button")
   element.click()

   el_id = element.get_attribute('id')
   el_text = element.get_attribute("onclick")
   l = el_text[8:16]

   assert el_id == l
print(f"A szöveg - '{l}"+" was clicked'- tartalmazza a gomb azonosítóját !" )
time.sleep(1)
driver.close()