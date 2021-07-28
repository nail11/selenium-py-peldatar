from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "http://localhost:9999/pagination.html"

try:
    driver.get(url)

    contact_table = driver.find_element_by_tag_name('tbody')
    persons = contact_table.find_elements_by_tag_name("tr")
    keys = driver.find_elements_by_xpath("//*[@id='contacts-table']/thead/tr/th")
    next_button = driver.find_element_by_id("next")
    persons_list = []

    while next_button.is_enabled():
        i = 0
        for i in range(len(persons)):
            person = persons[i].find_elements_by_tag_name("td")
            for j in range(1):
                first_name = person[1].text
                if first_name[0] == "J":
                    persons_data_dict = {
                    keys[1].text: person[1].text,
                    keys[2].text: person[2].text,
                    keys[3].text: person[3].text,
                    keys[4].text: person[4].text,
                    keys[5].text: person[5].text}
                    persons_list.append(persons_data_dict)
        print(persons_list)
        next_button.click()

        screen = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH,
            "/html/body")))


        #StaleElementReferenceException: Message: stale element reference: element is not attached to the page document


finally:
    driver.close()
