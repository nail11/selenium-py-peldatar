from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

# idő és dátum modul importálása !!!! Ez kell a dátummüveletekhez is a sleep()-hez is

from datetime import datetime, date, time, timezone

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()

driver.get("http://localhost:9999/forms.html")

now = datetime.now()

print(now)

# várunk egy kicsit, hogy lássuk kitöltetlenül a dátum mezőt
time.sleep(2)

# kiválasztjuk a dátum mezőt (Date) és elküldjük bele az aktuális idő dátum részét formázottan
# strftime('%m/%d/%Y') - mi a % jelentősége ?, year nagy Y !!

year = now.strftime('%Y')
month = now.strftime('%m')
day = now.strftime('%d')

print(f'{year} év')
print(f'{month} hónap')
print(f'{day} nap')

date_field = driver.find_element_by_id("example-input-date")

print(now.strftime('%d.%m.%Y'))
date_field.clear()
date_field.send_keys(now.strftime('%Y.%m.%d'))
