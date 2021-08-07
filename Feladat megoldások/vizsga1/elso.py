from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://proud-cliff-00bebe803.azurestaticapps.net/elso.html")

submit = driver.find_element_by_id('submit')


def get_age_in_seconds(age=None):
    age_field = driver.find_element_by_id('age')
    age_field.clear()
    if age != None:
        age_field.send_keys(age)
    submit.click()
    time.sleep(1)
    return driver.find_element_by_id('seconds').text


'''
  TC_001
  input: 39
  output in seconds: 1227376800
'''

assert get_age_in_seconds(39) == '1227376800'

'''
  TC_002
  input: 0
  output in seconds: 0
'''

assert get_age_in_seconds() == '0'

'''
  TC_003
  input: -112
  output in seconds: -3524774400
'''

assert get_age_in_seconds(-112) == '-3524774400'

driver.close()
