import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from datetime import datetime

options = Options()
prefs = {
    "download.default_directory": "C:\\Users\\tjozsa\\PycharmProjects\\homeworks\selenium2-homework"}

options.headless = False
options.add_experimental_option("prefs", prefs)

try:

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/another_form.html")

    submit_button = driver.find_element_by_id('submit')


    def type_into_field(field, data):
        if field == 'name':
            field = 'fullname'
        tmp_field = driver.find_element_by_id(f'{field}')
        tmp_field.clear()
        tmp_field.send_keys(data)


    with open('table_in.csv', encoding='utf-8') as csv_file:
        data = csv.DictReader(csv_file)
        for row in data:
            for key, value in row.items():
                if key != "DoB":
                    type_into_field(key.lower(), value.strip())
                else:
                    datetime_object = datetime.strptime(value, '%Y-%m-%d')
                    type_into_field(key.lower(), datetime_object.strftime("%m/%d/%Y"))
            submit_button.click()
            time.sleep(0.25)

    download = driver.find_element_by_tag_name('button')
    download.click()
    time.sleep(5)

    with open('table_in.csv', encoding='utf-8') as original:
        original_data = csv.DictReader(original)
        with open('table.csv', encoding='utf-8') as result:
            result_data = csv.DictReader(result)
            for row_orig, row_result in zip(original_data, result_data):
                for key_orig, value_orig in row_orig.items():
                    assert row_result[key_orig] == value_orig.strip()
finally:
    driver.close()
    driver.quit()
    os.remove("table.csv")