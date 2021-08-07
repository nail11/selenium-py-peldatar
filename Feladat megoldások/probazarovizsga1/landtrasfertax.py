from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html')
    time.sleep(2)

    # TC01:

    price_field = driver.find_element_by_id('price')
    go_button = driver.find_element_by_xpath('//button')
    tax_result = driver.find_element_by_id('tax')

    go_button.click()
    time.sleep(2)
    assert tax_result.get_attribute('value').strip() == ''
    assert driver.find_element_by_id('disclaimer').text == 'Enter the property value before clicking Go button.'

    # TC02:

    price_field.send_keys('33333')
    go_button.click()
    time.sleep(2)
    assert tax_result.get_attribute('value').strip() == '166.665'
    # A feladatban 16.665 volt megadva, de szrintem az csak elírás volt...

finally:
    driver.quit()
