from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
# ha a Chrome éa a chromedriver verzió illeszkedés kétséges - alapvetően mindíg

driver = webdriver.Chrome(ChromeDriverManager().install())
# ha a Chrome éa a chromedriver verzió illeszkedés kétséges - alapvetően mindíg

driver = webdriver.Chrome()

driver.get("https://www.google.com")

