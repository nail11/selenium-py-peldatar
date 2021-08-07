from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False
try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/alert_playground.html")


    def alert_action(prompt_text=''):
        alert = driver.switch_to.alert
        print(alert.text)
        if prompt_text.strip() != '':
            alert.send_keys(prompt_text)
        alert.accept()


    btns = driver.find_elements_by_tag_name('input')

    for btn in btns:
        prmpt = ''
        if btn.get_attribute('value') == 'Prompt':
            prmpt = 'Ezt figyeld!'

        if btn.get_attribute('value') != 'Double Click Me':
            btn.click()
            alert_action(prmpt)
        else:
            ac = ActionChains(driver)
            ac.double_click(btn).perform()
            alert_action()

    assert ('Ezt figyeld!' in driver.find_element_by_id('demo').text)
finally:
    driver.close()
    driver.quit()