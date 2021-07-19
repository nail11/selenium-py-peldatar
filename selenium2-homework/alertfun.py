# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan
# a selenium-py-peldatar alkalmazást. A program töltse be a példatárból az
# http://localhost:9999/alert_playground.html oldalt. A tanultak alapján az összes alert
# funkcióra írj selenium kódot. A prompt-nál teszteld le a be, hogy a beírt érték megjelenik-e egy
# paragraf tagben, miután eltűnt az alert.
# A megoldást egy alertfun.py nevű fileban kell beadnod.

from selenium import webdriver
import time

# a double click-hez ActionChains importja
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("http://localhost:9999/alert_playground.html")

try:

    # test texts
    alert_text = "I am alert"
    confirm_text = "I am confirm"
    double_click_text = "You double clicked me!!!, You got to be kidding me"
    test_text = "Ez OK!"

    alerts = [alert_text, confirm_text, double_click_text, test_text]
    print("print allerts:")
    print(alerts)

    # gombok megtalálása

    buttons = driver.find_elements_by_tag_name("input")
    print("buttons (as web elements)m and len of buttons list:")
    print(buttons)
    print(len(buttons))
    but_names = list()

    for i in range(len(buttons)):
        but_name = str(buttons[i].get_attribute("value"))
        but_names.append(but_name)
        but_name = []
        button_text = ""

    print("print the list of button names as string on the button")
    print(but_names)

    for i in range(len(buttons)):

        button = buttons[i] #driver.find_element_by_tag_name("input")
        print("prints the actual button as webelement - it changes as scrolls throgh the buttons list:")
        print(button)
        print("prints the actual buttons name")
        but_name = str(buttons[i].get_attribute("value"))
        print(but_name)

        if but_name == but_names[0]:
            driver.find_element_by_xpath("//input[contains(@value, but_name)]").click()
            at_button = driver.switch_to.alert
            time.sleep(2)
            print("prints at_button.text and alert")
            print(at_button.text)
            alert = at_button.text
            print(alert)
            print(alerts[0])
            assert alert == alerts[0]
            time.sleep(2)
            at_button.accept()

        if but_name == but_names[1]:
            driver.find_element_by_xpath("//input[contains(@value, but_name)]").click()
            at_button = driver.switch_to.alert
            time.sleep(1)
            print("prints at_button.text and alert")
            print(at_button.text)
            alert = at_button.text
            print(alert)
            print(alerts[1])
            assert (alert == alerts[1])
            time.sleep(1)
            at_button.accept()

    alert = driver.find_element_by_name("alert")
    confirm = driver.find_element_by_name("confirmation")
    prompt = driver.find_element_by_name("prompt")
    double_click = driver.find_element_by_id("double-click")

    prompt_text = driver.find_element_by_id('demo').text

    # def

    # testing alert button
    alert.click()
    at_alert = driver.switch_to.alert
    assert (at_alert.text == alert_text)
    print(at_alert.text)
    at_alert.accept()

    # testing confirmation button
    # confirmation accept
    confirm.click()
    at_confirm = driver.switch_to.alert
    assert (at_confirm.text == confirm_text)
    print(at_confirm.text)
    at_confirm.accept()

    # confirmation dismiss
    confirm.click()
    at_confirm = driver.switch_to.alert
    assert (at_confirm.text == confirm_text)
    at_confirm.dismiss()

    # testing double_click button

    # az ActionChains-nek átadjuk a driver-t
    action = ActionChains(driver)
    action.double_click(double_click).perform()
    at_double_click = driver.switch_to.alert
    assert (at_double_click.text == double_click_text)
    print(at_double_click.text)
    at_double_click.accept()

    # testing prompt button
    prompt.click()
    at_prompt_but = driver.switch_to.alert
    prompt.send_keys(test_text)
    at_prompt_but.accept()
    print(test_text)
    print(prompt_text)
    assert prompt_text == test_text


finally:
    # driver.close()
    pass
