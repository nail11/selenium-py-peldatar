from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/kitchensink.html")

# látható-e egy elem - is_displayed() és hasonlók kipróbálása
try:
    input_text = driver.find_element_by_id("displayed-text")
    hidebutton = driver.find_element_by_id("hide-textbox")
    showbutton = driver.find_element_by_id("show-textbox")
    print(input_text.is_displayed())
    hidebutton.click()
    print(input_text.is_displayed())
finally:
    driver.close()