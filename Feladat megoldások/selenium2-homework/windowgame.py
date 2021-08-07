import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random

opt = Options()

opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/windowgame.html")

target_color = driver.find_element_by_id('target_color').text

button_list = driver.find_elements_by_tag_name('button')

main_window_handle = driver.window_handles[0]

while True:
    button_index = random.randint(0, len(button_list)-1)
    button_id = button_list[button_index].get_attribute('id')
    button_list[button_index].click()
    new_window_handle = driver.window_handles[1]
    driver.switch_to.window(new_window_handle)
    color = driver.find_element_by_tag_name('h1').text
    if color == target_color:
        print('Gomb megtalálva!')
        print(f'Button elem id-ja: {button_id}')
        break
    else:
        button_list.pop(button_index)
        driver.close()
        driver.switch_to.window(main_window_handle)

print(f'Kattintott gombok száma: {100-len(button_list)}')

driver.close()