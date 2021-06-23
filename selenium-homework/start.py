import selenium

pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager import ChromeDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("https://www.google.com")
# driver.find_element_by_css_selector("img").get_attribute("alt")
# 'Google'