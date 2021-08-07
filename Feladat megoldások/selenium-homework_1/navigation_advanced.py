from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/general.html")
    links = driver.find_elements_by_xpath('//a')

    for i in links:
        if i.text == '#':
            links.remove(i)

    for i in range(len(links)):
        link = driver.find_elements_by_xpath("//a")[i]
        val = link.get_attribute('href')
        if link.get_attribute('target'):
            win = driver.window_handles[0]
            link.click()
            driver.switch_to.window(driver.window_handles[1])
            if driver.current_url == val:
                print("Good URL")
                print(driver.current_url)
                print(val)
            else:
                print("Bad URL")
                print(driver.current_url)
                print(val)
            driver.close()

            driver.switch_to.window(win)
        else:
            link.click()
            if driver.current_url == val:
                print("Good URL")
                print(driver.current_url)
                print(val)
            else:
                print("Bad URL")
                print(driver.current_url)
                print(val)
            driver.back()
except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()
