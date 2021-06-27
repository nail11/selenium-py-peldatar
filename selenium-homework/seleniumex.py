from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.python.org")

try:
    driver.find_element_by_id("nemletezik")

except:
    print("A 'nemlétezik' azonosítójú elem nem létezik")

finally:
    driver.close()

# 'nemlétező elem' hibát kezelő függvény a seleniumex_fun.py file-ben



