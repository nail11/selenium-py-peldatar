import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/todo.html")

try:
    todo_s = driver.find_elements_by_xpath('//*[@class="done-false"]')
    for todo in todo_s:
        print("TODO:"+ todo.text)
except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()

