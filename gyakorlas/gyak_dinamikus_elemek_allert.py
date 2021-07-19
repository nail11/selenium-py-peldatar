from selenium import webdriver
import time

driver = webdriver.Chrome()

# driver.switch_to ablakváltás és az alert. utasítás használata
try:
    driver.get("http://localhost:9999/kitchensink.html")

    name = driver.find_element_by_id('name').send_keys('Laci')
    button = driver.find_element_by_id('alertbtn').click()
    ref_text = "Hello Laci, share this practice page and share your knowledge"
    alert = driver.switch_to.alert
    assert (alert.text == ref_text)
    print(alert.text)
    time.sleep(2)
    alert.accept()
    time.sleep(2)

finally:
    driver.close()
    pass
