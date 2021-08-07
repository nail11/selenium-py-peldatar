from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import time

ua = 'Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
header = {'User-Agent': ua}

opt = Options()

opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/scrolltoload.html")


def get_url_and_id(element):
    out = dict()
    out['url'] = element.find_element_by_tag_name('img').get_attribute('src')
    out['id'] = element.find_element_by_tag_name('p').text.replace('Cat id: ', '')
    return out


# check cats directory exists, if not create it
if not os.path.isdir('cats'):
    os.mkdir('cats')

# get more images
tmp = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'img')))
time.sleep(1)  # ez muszáj, különben a send_keys(Keys.PAGE_DOWN) nem működik
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.PAGE_DOWN)
time.sleep(2)  # ez muszáj, hogy az elemek elkezdjenek megjelenni a lapon, amire a WebDriverWait várhat.
# get all images in a list
image_list = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'image')))

print(f'Length of the list of images (after a ton of wait...) : {len(image_list)}')

# download and save images
assert len(image_list) >= 20
for i in range(20):
    cat_pic_url = get_url_and_id(image_list[i])['url']
    cat_id = get_url_and_id(image_list[i])["id"]
    img_extension = cat_pic_url[-3:]
    out_file = f'cats/{i}_{cat_id}.{img_extension}'
    img_stream = requests.get(cat_pic_url, headers=header)
    with open(out_file, 'wb') as img_file:
        img_file.write(img_stream.content)
    print(f'{out_file} saved successfully')
driver.quit()