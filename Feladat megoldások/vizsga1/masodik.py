from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://proud-cliff-00bebe803.azurestaticapps.net/masodik.html")


def unit_converter(numb, unit):
    num_field = driver.find_element_by_id('number')
    num_field.clear()
    num_field.send_keys(numb)
    unit_field = driver.find_element_by_id('unit')
    unit_field.clear()
    unit_field.send_keys(unit)
    return driver.find_element_by_class_name('conversion').text


'''
  TC_001: 
  input_1: 112
  input_2: meter
  result: 367.45406824146977 FOOT
'''

assert unit_converter(112, 'meter') == '367.45406824146977 FOOT'

'''
  TC_002: 
  input_1: 8
  input_2: oz
  result: 236.56 MILLILITER
'''

assert unit_converter(8, 'oz') == '236.56 MILLILITER'

'''
  TC_003: 
  input_1: 1
  input_2: gallon
  result: 3.785 LITER
'''

assert unit_converter(1, 'gallon') == '3.785 LITER'

driver.close()
