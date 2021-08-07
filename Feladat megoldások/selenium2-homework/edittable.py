from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from random import choice  # listából véletlenszerűen választ

options = Options()

options.headless = False
try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/editable-table.html")

    data = [('DELL laptop', '300.5', '5', 'Electronics'), ('Microsoft Windows', '10', '100', 'Software')]

    add_row = driver.find_element_by_tag_name('button')
    sleep_time = 0

    def refresh_rows_list(class_name):
        return driver.find_elements_by_class_name(class_name)


    def fill_row(row, name, price, qty, cat):
        row.find_element_by_name('name').clear()
        row.find_element_by_name('name').send_keys(name)
        row.find_element_by_name('price').clear()
        row.find_element_by_name('price').send_keys(price)
        row.find_element_by_name('qty').clear()
        row.find_element_by_name('qty').send_keys(qty)
        row.find_element_by_name('category').clear()
        row.find_element_by_name('category').send_keys(cat)


    def del_row(row):
        row.find_element_by_class_name('del-btn').click()


    def add_rows(number_of_rows, data_list):
        for i in range(number_of_rows):
            add_row.click()
            rows_list = refresh_rows_list('eachRow')
            fill_row(rows_list[len(rows_list) - 1], *data_list[i])


    def search_element(txt):
        search_box = driver.find_element_by_tag_name('input')
        search_box.clear()
        search_box.send_keys(txt)
        return refresh_rows_list('eachRow')


    # 2 sor hozzáadása
    add_rows(2, data)
    time.sleep(sleep_time)

    # sortörlés csak úgy, hogy ezt is kipróbáljam
    del_row(choice(refresh_rows_list('eachRow')))
    time.sleep(sleep_time)

    # Keresőmező ellenőrzése
    search_string = 'bas'

    for row in search_element(search_string):
        assert search_string in row.find_element_by_name('name').get_attribute('value')

    time.sleep(sleep_time)
    # frissítjük az oldalt alaphelyzetbe hozásra
    driver.refresh()

    time.sleep(sleep_time)
    # mezők átírása, DOM ellenőrzés
    data_mod_test = [('Samsung monitor', '15.99', '3', 'Electronics')]
    rows_in_table = refresh_rows_list('eachRow')
    selected_row = choice(rows_in_table)
    fill_row(selected_row, *data_mod_test[0])
    x = 0
    for inp in selected_row.find_elements_by_tag_name('input'):
        assert inp.get_attribute('value') == data_mod_test[0][x]
        x += 1
        if x >= 3:
            break

    time.sleep(sleep_time)

finally:
    driver.close()
    driver.quit()