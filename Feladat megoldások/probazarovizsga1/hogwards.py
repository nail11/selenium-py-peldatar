from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html")
    time.sleep(2)

    # Feltöltendő adatok megadása
    name = 'HARRY POTTER'
    date_dep = '002021-10-14'
    time_dep = '12:00PM'

    # Adatok felvitele a mezőkbe és 'issue ticket gomb megnyomása
    driver.find_element_by_id('passenger').send_keys(name)
    driver.find_element_by_id('departure-date').send_keys(date_dep)
    driver.find_element_by_id('departure-time').send_keys(time_dep)
    driver.find_element_by_id('issue-ticket').click()
    time.sleep(3)

    # Megjelenő adatok kigyűjtése
    passenger_name = driver.find_element_by_id('passenger-name').text
    departure_date = driver.find_element_by_id('departure-date-text').text
    side_departure_date = driver.find_element_by_id('side-detparture-date').text
    departure_time = driver.find_element_by_id('departure-time-text').text
    side_departure_time = driver.find_element_by_id('side-departure-time').text

    # Megjelenő adatok összevetése a bevitt adatokkal
    assert name == passenger_name
    assert date_dep == '00' + departure_date == '00' + side_departure_date
    # Azért kell a '00', mert a mező csak így fogadta be megfelelően a dátumot (14. sor)
    assert time_dep == departure_time == side_departure_time

finally:
    driver.close()
