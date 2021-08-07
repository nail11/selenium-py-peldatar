from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
try:
    driver.get("https://blue-rock-04e841a03.azurestaticapps.net/masodik.html")
    # create new todo
    todo_text = "This is the new todo text"
    driver.find_element_by_xpath('//*[@id="new-todo-input"]').send_keys(todo_text)
    driver.find_element_by_xpath('//*[@id="new-todo-button"]').click()
    todo_items = driver.find_elements_by_xpath('//li[@name="todo-item"]/span')
    assert len(todo_items) == 6
    assert todo_text in [item.text for item in todo_items]

    # mark todo completed:
    todo_items = driver.find_elements_by_name("todo-item")
    item_input = driver.find_element_by_xpath('//li[@name="todo-item"]/input')
    item_text = driver.find_element_by_xpath('//li[@name="todo-item"]/span')
    assert item_text.get_attribute("class") == 'done-false'
    item_input.click()
    assert item_text.get_attribute("class") == 'done-true'
    assert len(driver.find_elements_by_name("todo-item")) == 6

    # archive done todos
    assert len(driver.find_elements_by_name("todo-item")) == 6
    driver.find_element_by_xpath('//div[@class="container"]//a').click()
    assert len(driver.find_elements_by_name("todo-item")) == 5
finally:
    driver.close()
    driver.quit()
