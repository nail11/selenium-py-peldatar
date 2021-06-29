from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/trickyelements.html")

for i in range(1, 6):

   element_list = (driver.find_element_by_id( 'element'+str(i)))

print(element_list)