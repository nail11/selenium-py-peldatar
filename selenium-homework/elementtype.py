from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/trickyelements.html")

element_list = [driver.find_element_by_id('element1'), driver.find_element_by_id('element2'). driver.find_element_by_id('element3'), driver.find_element_by_id('element4'), driver.find_element_by_id('element5')]

print(element_list)
