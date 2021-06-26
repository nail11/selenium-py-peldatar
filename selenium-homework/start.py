from selenium import webdriver

# from selenium.webdriver.chrome.options import Options

# from webdriver_manager import ChromeDriverManager
# ha a Chrome éa a chromedriver verzió illeszkedés kétséges - alapvetően mindíg

# options = Options()
# options.add_argument("--headless")
# options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
# ha a Chrome éa a chromedriver verzió illeszkedés kétséges - alapvetően mindíg

driver = webdriver.Chrome()

driver.get("https://www.google.com")
# 'Google'
