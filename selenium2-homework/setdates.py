# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt
# filenevet. Ezen a néven fogadható el a megoldás.
# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar
# alkalmazást. A program töltse be a példatárból az http://localhost:9999/forms.html oldalt.
# Koncentrálj a dátum mezőkre.
# A célod, hogy a következő képen látható dátum és idő értékekete pontosan beállítsd az alkalmazásba
# selenium segítségével:
# A megoldást egy setdates.py nevű fileban kell beadnod.

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, date

driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()

driver.get("http://localhost:9999/forms.html")

date = date(2021, 5, 6)
driver.find_element_by_id("example-input-date").send_keys(date.strftime("00%Y.%m.%d"))

date_time = datetime(2012, 5, 5, 5, 5, 5, 555)
driver.find_element_by_id("example-input-date-time").send_keys(
    date_time.strftime("%Y.%m.%d %H:%M:%S:%f").replace("000", ""))

date_time_local = datetime(2000, 12, 5, 12, 1)
driver.find_element_by_id("example-input-date-time-local").send_keys(date_time_local.strftime("00%Y/%m/%d%I%M\t%p"))

month = datetime(1995, 12, 1)
driver.find_element_by_id("example-input-month").send_keys(month.strftime("%Y\t%B"))

week = datetime(2015, 12, 30)
driver.find_element_by_id("example-input-week").send_keys(week.strftime("%W%Y"))

time = datetime(2000, 1, 1, 12, 25)
driver.find_element_by_id("example-input-time").send_keys(time.strftime("%H:%M"))
# AM/PM nem jön elő

driver.close()
