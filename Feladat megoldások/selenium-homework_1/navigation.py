from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    base_url = "http://localhost:9999/general.html"
    driver.get(base_url)
    links = driver.find_elements_by_xpath('//a')

    for i in links:
        if i.text == '#':
            links.remove(i)

    for link in links:
        val = link.get_attribute('href')
        if link.get_attribute('target'):
            if base_url in val:
                link.click()
                print("Good URL")
                print(val)
                driver.back()
            else:
                print("Bad URL")
                print(val)
                print("not visiting!!!!")
        else:
            if base_url in val:
                link.click()
                print("Good URL")
                print(val)
                driver.back()
            else:
                print("Bad URL")
                print(val)
                print("not visiting!!!!")

except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()
