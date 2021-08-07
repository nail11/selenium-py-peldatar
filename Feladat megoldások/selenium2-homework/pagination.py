import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False
try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/pagination.html")

    collected_data = []

    head = [th.text for th in driver.find_elements_by_xpath('//table[@id="contacts-table"]/thead/tr/th')]

    while True:
        for tr in driver.find_elements_by_xpath('//table[@id="contacts-table"]/tbody/tr'):
            td_texts_list = [td.text for td in tr.find_elements_by_tag_name('td')]
            row = dict(zip(head, td_texts_list))
            if row['First name'].startswith('A'):
                collected_data.append(row)

        next_btn = driver.find_element_by_id('next')

        if next_btn.is_enabled():
            next_btn.click()
        else:
            break

    with open('start_with_A.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=head)
        writer.writeheader()
        for data_row in collected_data:
            writer.writerow(data_row)
finally:
    driver.close()
    driver.quit()