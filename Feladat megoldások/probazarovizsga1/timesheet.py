from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html')
    time.sleep(2)

    # TC01:

    next_button = driver.find_element_by_xpath('//*[@id="buttons"]/input')
    assert not next_button.is_enabled()
    time.sleep(2)

    # Kitöltendő mezők kinyerése:

    email_field = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[1]')
    hours_field = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[2]')
    minutes_field = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[3]')
    message_field = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/textarea')
    types_of_work = driver.find_element_by_xpath('//*[@id="dropDown"]/option')

    email_valid = 'test@bela.hu'
    email_invalid = 'testvbela'
    hours = '2'
    minutes = '0'
    message = 'working hard'

    # Mezők kitöltése
    email_field.send_keys(email_invalid)
    hours_field.send_keys(hours)
    minutes_field.send_keys(minutes)
    message_field.send_keys(message)
    types_of_work.click()
    time.sleep(2)

    assert not next_button.is_enabled()
    time.sleep(2)

    # TC02:

    # Clear button megnyomása
    driver.find_element_by_xpath('//*[@id="buttons"]/button').click()

    # Mezők kitöltése
    email_field.send_keys(email_valid)
    hours_field.send_keys(hours)
    minutes_field.send_keys(minutes)
    message_field.send_keys(message)
    types_of_work.click()
    time.sleep(2)

    next_button.click()
    time.sleep(2)

    # Megjelenő tartalom ellenőrzése
    assert driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[1]').text == '2'
    assert driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[2]').text == '0'

finally:
    driver.close()
