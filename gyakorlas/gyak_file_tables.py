from selenium import webdriver
import csv

# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()

driver.get("http://localhost:9999/filltablewithsum.html")


def find_element_by_id(id):
    element = driver.find_element_by_xpath(id)
    element.clear()
    return element


with open('data.csv', 'r') as table_data:
    table = csv.reader(table_data, delimiter=',')
    next(table)
    for row in table:
        find_element_by_id('product').send_keys(row[0])
        find_element_by_id('quantity').send_keys(row[1])
        find_element_by_id('price').send_keys(row[2])
        driver.find_element_by_id('add').click()

totals = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/div')
print(totals.text)  # itt jelenik meg a .text kifejezés először

results = driver.find_elements_by_xpath('//*[@id="results"]/tbody/tr')

with open('data_ex.txt','w') as data_ex:

    for row in results:

        cells = row.find_elements_by_tag_name('td')
        data_ex.write(cells[0].text+','+cells[1].text+','+cells[2].text+'\n')
        print(cells[0].text, cells[1].text, cells[2].text)

driver.close()




