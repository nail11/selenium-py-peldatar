# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a
# selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999 oldalt. Lokátorral keresd ki az összes linket az oldalról.
# Tárold a memóriában egy listában az összes linket. A list tartalmát írd ki egy fájlba. Minden link egy új sorba
# kerüljön. A kimenetre írd ki hány linket találtál
# A megoldást egy linkek.py nevű file-ban kell beadnod.

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()

driver.get("http://localhost:9999")

html_refs = driver.find_elements_by_css_selector('body > div > table > tbody > tr > td > a')

# driver.find_elements_by_css_selector(.....) visszaadja a html-t tartalmazó elemek listáját -> html_refs
# beállítjuk a számlálót

ref_count = 0

with open('html_refs.txt', 'w') as text:
    # html_refs.txt fájlban tároljuk majd a html listát

    for html in html_refs:
        # végigmegyünk a html_refs lista elemein

        text.write(html.get_attribute('href') + '\n')

        # és beírjuk a lista elemeihez tartozó 'href' attributum tartalmát
        # (l. Stackoverflow, Python Selenium - get href value) -> html
        # minden elemnél a számlálóhoz adunk plusz 1-t

        ref_count += 1

driver.close()

# print(html_refs)
print(str(ref_count) + ' db linket találtam')
