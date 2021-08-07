from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://blue-rock-04e841a03.azurestaticapps.net/elso.html")

def locate_calc_button(text):
    if text == 'AC':
        return driver.find_element_by_xpath(f'//button[@class="calculator-key key-clear"]')
    else:
        return driver.find_element_by_xpath(f"//button[text() = '{text}']")

def locate_result():
    return driver.find_element_by_xpath('//div[@class="calculator-display"]/div[text()]')

def percent(a):
    for c in str(a):
        locate_calc_button(c).click()
        time.sleep(0.2)
    locate_calc_button('%')
    locate_calc_button('=')
    return locate_result().text

def calculate(a,op,b):
    locate_calc_button('AC').click()
    for c in str(a):
        locate_calc_button(c).click()
        time.sleep(0.2)
    locate_calc_button(op).click()
    for c in str(b):
        locate_calc_button(c).click()
    locate_calc_button('=').click()
    return locate_result().text
try:
    assert calculate('99', '+', '1') == '100'

    assert calculate('−5', '+', '5') == '0'

    assert calculate('1', '+', '2') == '3'
    locate_calc_button('c').click()
    assert locate_result().text == '0'

    locate_calc_button('1').click()
    locate_calc_button('c').click()
    assert locate_result().text == '0'
finally:
    driver.close()
    driver.quit()