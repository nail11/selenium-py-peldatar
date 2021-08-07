from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()

options.headless = False
try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/simplevalidation.html")

    validation = [("test-email", "Please enter an e-mail"), ("test-password", "This field can't be empty"),
           ("test-confirm-password", "Please complete Desired Password"),
           ("test-customer-number", "This field can't be empty"),
           ("test-dealer-number", "This field can't be empty"),
           ("test-random-field", ""),
           ("test-date-field", "This field can't be empty"),
           ("test-url-field", ""),
           ("test-random-textarea", "This field can't be empty"),
           ("test-card-type", "Please select a card type"),
           ("test-card-number", "Please enter a credit card number (no spaces)"),
           ("test-card-cvv", "This field can't be empty"),
           ("test-card-month", "Select a month"),
           ("test-card-year", "Select a year"),
           ("test-single-checkbox", "This field can't be empty"),
           ("test-save-email-yes", "Please select one"),
           ("test-terms-service", "Please agree to both to continue"),
           ("test-terms-service-more", "Please agree to both to continue")]

    def get_element_error_msg(element, inp):
        tmp = driver.find_element_by_id(element)
        tmp.send_keys(inp)
        attr = tmp.get_attribute("data-jsv-message-target")
        time.sleep(1)
        try:
            out = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
                (By.XPATH, '//div[@id="{}"]'.format(attr)))).text
        except TimeoutException:
            out = None
        return out


    # Tesztelés üres mezőkkel
    for id, error in validation:
        e = get_element_error_msg(id, '\t')
        if e is not None:
            assert e == error
            print(f'id={id} mező tesztelve, a(z) >>{e}<< üzenet megjelent! ')
        else:
            print(f'id={id} mező tesztelve, nincs hibaüzenet!')
finally:
    driver.close()
    driver.quit()
