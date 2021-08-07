from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html')
    time.sleep(2)

    # TC01

    # Gombok az oldalon
    subtotal_btn = driver.find_element_by_id('subtotalBtn')
    calculate_order_btn = driver.find_element_by_id('gtotalBtn')

    subtotal_btn.click()
    calculate_order_btn.click()

    # Mezők elmentése
    subtotal = driver.find_element_by_id('subtotal')
    total = driver.find_element_by_id('gtotal')
    tax = driver.find_element_by_id('salestax')

    assert subtotal.get_attribute('value').strip() == '0.00'
    assert total.get_attribute('value') == '4.95'

    # TC02

    # Legördülő menü kezelése
    product_item = driver.find_element_by_id('Proditem')
    product_item.click()
    product_item.send_keys(Keys.ARROW_DOWN)
    product_item.send_keys(Keys.ENTER)

    # Tesztadatok beküldése
    driver.find_element_by_id('quantity').send_keys('1')

    # Ahhoz, hogy kitöltődjön a feladatban leírt mező 'salastax' ezt be kell pipálni
    driver.find_element_by_id('billState').click()

    subtotal_btn.click()
    calculate_order_btn.click()

    # Viszont, ha bepipáltam, az értékek megváltoznak az alábbiakra, ezt számológéppel ellenőriztem.
    assert tax.get_attribute('value').strip() == '0.43'
    assert total.get_attribute('value').strip() == '10.33'

finally:
    driver.close()
