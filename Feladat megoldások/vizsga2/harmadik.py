from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
try:
    driver.get("https://blue-rock-04e841a03.azurestaticapps.net/harmadik.html")

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    which_exercise_input = driver.find_element_by_id("which_exercise")
    which_exercise_input.send_keys('harmadik')
    mehet_button = driver.find_element_by_xpath('//button[text()="Mehet"]')
    mehet_button.click()
    secret_pass = driver.find_element_by_id('secret-pass')

    assert secret_pass.text in months

    currrent_secret_password_input = driver.find_element_by_id("currrent_secret_password")
    currrent_secret_password_input.send_keys(secret_pass.text)
    ellenoriz_button = driver.find_elements_by_xpath('//button[text()="Ellenőriz"]')[0]
    ellenoriz_button.click()
    secret_pass_check_result = driver.find_element_by_id("secret-pass-check-result")
    assert secret_pass_check_result.text == "Nyert!"

    equasion = driver.find_element_by_xpath('//label[@for="result"]').text.strip().split('=')[1]
    sub_eq = equasion.split('+')
    sub_eq2 = sub_eq[1].split('/')
    a = int(sub_eq[0])
    b = int(sub_eq2[0])
    c = int(sub_eq2[1])
    result_input = driver.find_element_by_id("result").send_keys(str(int(a + b / c)))
    ellenoriz_button = driver.find_elements_by_xpath('//button[text()="Ellenőriz"]')[1]
    ellenoriz_button.click()
    assert driver.find_element_by_id("result-return").text == 'Jó az eredmény!'

finally:
    driver.close()
    driver.quit()
