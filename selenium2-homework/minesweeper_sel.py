# Egy kis játékra invitállak. Feladatod, hogy selenium segítségével megnyerd az aknakereső játékot.
#
# Készíts egy Python alkalmazást ami selenium-ot használ. Készíts egy Python alkalmazást ami selenium-ot
# használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A program töltse be a példatárból
# az http://localhost:9999/minesweeper-game.html oldalt. A feladat egyszerű éld túl az aknamezőt.
# A selenium python programnak kell automatikusan végigjétszania a játékot. A megoldáshoz használhattsz más
# könyvtárakat is pl: https://github.com/madewokherd/mines
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()

driver.get("http://localhost:9999/minesweeper-game.html")

# mine = driver.find_elements_by_class_name('covered')
# mine = driver.find_elements_by_class_name('mines1')
covered = driver.find_elements_by_css_selector('div.covered')

for i in range(len(covered)):
    covered[i].click()
    covered = driver.find_elements_by_css_selector('div.covered')
    if covered[i].get_attribute('div') == 'mine':
            print(covered[i].get_attribute('div'))
            print('A játéknak vége !')
    else:
            i += 1
print(type(covered))
# mine.click()
print(len(covered))
# print(mine.get_attribute('class'))
