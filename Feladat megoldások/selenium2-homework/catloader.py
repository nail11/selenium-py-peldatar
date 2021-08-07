from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import time

ua = 'Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
header = {'User-Agent': ua}

options = Options()

options.headless = False
try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/loadmore.html")


    def get_url_and_id(element):
        out = dict()
        out['url'] = element.find_element_by_tag_name('img').get_attribute('src')
        out['id'] = element.find_element_by_tag_name('p').text.replace('Cat id: ', '')
        return out


    # check cats directory exists, if not create it

    if not os.path.isdir('cats'):
        os.mkdir('cats')

    # get the more images button
    more_images_btn = driver.find_element_by_xpath('//div[@class="load-more-button"]/button')

    # and click it 4 times
    for i in range(4):
        time.sleep(2)
        more_images_btn.click()

    # get all images in a list
    image_list = driver.find_elements_by_class_name('image')
    time.sleep(5)

    # download and save images
    for i in range(len(image_list)):
        cat_pic_url = get_url_and_id(image_list[i])['url']
        cat_id = get_url_and_id(image_list[i])["id"]
        img_extension = cat_pic_url[-3:]
        out_file = f'cats/{i}_{cat_id}.{img_extension}'
        img_stream = requests.get(cat_pic_url, headers=header)
        with open(out_file, 'wb') as img_file:
            img_file.write(img_stream.content)
finally:
    driver.close()
    driver.quit()