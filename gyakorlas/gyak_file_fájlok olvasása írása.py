# environment settings
#......................................................................

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
# from selenium.webdriver.common.keys import Keys
# from datetime import date
# import time
# from pathlib import Path
# import pprint

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# In order for ChromeDriverManager to work you must pip install it in your own environment.

# driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#url = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"

try:
    # fájlok olvasása-írása

    with open("vmi.txt", "w") as f:
        f.write("ezt írom bele a vmi fájlba")

    # "w" irás, "r" olvasás, "bw" bitenkénti írás pl. képek, "a" hozzáfűzés

    # "f" (lehet bármi) egy python object példánya, a megnyitott txt-re mutató referencia amin mindenféla
    # műveletet tudunk végezniés ezen keresztül manipuláljuk a fájl tatalmát

    # a következőkben kiíratom a vmi.txt fájl tartalmát (az "f"-en keresztül azaz az f-et) egy result nevű
    # változóba és kiprintelem

    with open("vmi.txt", "r") as f:
        result = f.read()
        print("ez a 'result' változónól jön")
        print(result)

    with open("vmi.txt", "a") as f:
        f.write("- ezt fűztem hozzá")

    # előbb hozzáfúztem néhány szót a vmi.txt tartalmához

    # with open("vmi.txt", "r") as f:
        #result = f.readlines()
    # egy listába irja a sorokat, mint a lista elemeit

    # with open("vmi.txt", "r") as f:
    # result = f.readline()
    # egy sort olvas be szövegként

    # végig iterálhatok az "f"-en
    # for line in f
        # itt a "line" a  sorokat jeleneti


    # ha az előző blokkban ismét használni akarom a fájlt akkor az hibát eredményez, amit nem jelez a program
        #with open("vmi.txt......)


finally:
    pass