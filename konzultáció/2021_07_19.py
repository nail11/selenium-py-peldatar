## Rossz megoldas
# name = "Tamas"
# name2 = "Gabor"
# name3 = "Nora"
# Nem annyira rossz megodas
# names = ["Tamas", "Gabor", "Nora"]
# neg_names = [0, None, ""]
# Jo megoldas


# 3         --> int     => int()
# "Tamas"   --> str     => str()
# 3.14      --> float   => float()
# True      --> bool    => bool()
# class int:
#     def __init__(self, value):
#         self.value = value
# tervrajzt az a osztály (class)
# epulet az a példány (instance, object)
class NameTestData:
    def __init__(self, firt_name, quantity=0, last_name=""):
        self.firt_name = firt_name
        self.quantity = quantity
        self.last_name = last_name
        # self.full_name = f"{self.firt_name} {self.last_name}"
    def __str__(self):
        return f"*NameTestData({self.firt_name}, {self.quantity})"
    def __repr__(self):
        return f"!NameTestData({self.firt_name}, {self.quantity})"
    def full_name(self):
        return f"{self.firt_name} {self.last_name}"

nj = NameTestData("Janos", 11, "Nagy")
print(nj)
test_data = [NameTestData("Tamas", 15, "Jozsa"), NameTestData("Gabor"), NameTestData("Nora")]
print(test_data)
for data in test_data:
    print(data.full_name())



# a csv-ből feltöltő feladathoz készítünk osztályt (csv-ből töltjük fel, és ezt használjuk adatbevitelre
#táblafeltöltés példából az adatok objektumát csináltuk meg

import csv
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pprint
# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element

class Product:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
    def __repr__(self):
        return f"Product({self.product_name, self.quantity, self.price})"

def load_products_from_csv():
    product_list = []
    with open('data.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # skip header
        for row in csvreader:
            product_list.append(Product(row[0], row[1], row[2]))
    return product_list
try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/filltablewithsum.html")
    products = load_products_from_csv()
    pprint.pprint(products)
    for product in products:
        find_and_clear_by_id("product").send_keys(product.product_name)
        find_and_clear_by_id("quantity").send_keys(product.quantity)
        find_and_clear_by_id("price").send_keys(product.price)
        driver.find_element_by_id("add").click()
finally:
    driver.close()