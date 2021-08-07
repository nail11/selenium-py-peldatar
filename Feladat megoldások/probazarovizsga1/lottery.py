from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html')
    time.sleep(2)

    # TC01:
    lottery_numbers = driver.find_elements_by_xpath('//*[@class="balls"]')
    assert lottery_numbers == []
    time.sleep(2)

    # TC02:
    generate_button = driver.find_element_by_id('draw-number')

    # 6 db szám ellenőrzése
    for i in range(6):
        generate_button.click()
        time.sleep(2)
    lottery_numbers = driver.find_elements_by_xpath('//*[@class="balls"]')
    assert len(lottery_numbers) == 6

    # Számok értékének ellenőrzése
    for i in lottery_numbers:
        assert 0 < int(i.text) < 60

    # TC03:
    generate_button.click()

    # A hetedik szám nemlétének ellenőtzése
    lottery_numbers = driver.find_elements_by_xpath('//*[@class="balls"]')
    assert len(lottery_numbers) == 6
    time.sleep(2)

    # Reset után ellenőrzés, hogy nincs szám kihúzva
    driver.find_element_by_id('reset-numbers').click()
    lottery_numbers = driver.find_elements_by_xpath('//*[@class="balls"]')
    assert lottery_numbers == []

finally:
    driver.close()
