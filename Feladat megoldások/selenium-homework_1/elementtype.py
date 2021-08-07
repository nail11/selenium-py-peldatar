from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/trickyelements.html")
    found_elements = [driver.find_element_by_id("element1"), driver.find_element_by_id("element2"), driver.find_element_by_id("element3"),
                      driver.find_element_by_id("element4"), driver.find_element_by_id("element5")]
    for element in found_elements:
        if element.tag_name == "button" or element.get_attribute("onclick") is not None:
            button_text = element.text
            element.click()
            break
    message_text = driver.find_element_by_id("result").text
    assert f'{button_text} was clicked' == message_text
    print("test finished OK")

except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()
