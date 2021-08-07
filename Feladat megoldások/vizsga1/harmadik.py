from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://proud-cliff-00bebe803.azurestaticapps.net/harmadik.html")

btn_heads = driver.find_element_by_id('heads')
btn_tails = driver.find_element_by_id('tails')

input_money = driver.find_element_by_id('cash')
input_bet = driver.find_element_by_id('bet')
output_result = driver.find_element_by_id('outcome')

'''
  TC_000:
  Money: 100
  Bet: <üres>
  Result: -
'''

assert input_money.get_attribute("value").strip() == '100' and input_bet.get_attribute(
    "value").strip() == '' and output_result.text.strip() == '-'

'''
  TC_001:
  Bet:10
  Tails megnyom
  Result: heads vagy tails
  ha eltaláltuk:
    Money: 110
  ha nem találtuk el:
    Money: 90
'''

input_bet.clear()
input_bet.send_keys(10)
btn_tails.click()

assert (input_money.get_attribute("value").strip() == '110' or input_money.get_attribute("value").strip() == '90') and (
            output_result.text.strip() == 'heads' or output_result.text.strip() == 'tails')

driver.close()
