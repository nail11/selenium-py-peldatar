# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a
# selenium-py-peldatar alkalmazást. A program töltse be a példatárból az http://localhost:9999/editable-table.html
# oldalt. A megjelenő táblázatban az alábbi feladatokat kell végrehajtanod: a) Addj hozzá még két teljsen
# kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok. b) Ellenőrizd a kereső funkciót.
# c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.
# A megoldást egy edittable.py nevű fileban kell beadnod.

from selenium import webdriver
import csv

# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()

driver.get("http://localhost:9999/editable-table.html")