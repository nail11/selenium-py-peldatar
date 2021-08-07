from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/')

links = driver.find_elements_by_xpath('//a')

try:
    link_count = 0
    with open('links.txt', 'w') as text_file:
        for link in links:
            text_file.write(link.get_attribute('href') + '\n')
            link_count += 1

    print(f'number of links found on the page: {link_count}')
finally:
    driver.close()
    driver.quit()