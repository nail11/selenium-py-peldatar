import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/forms.html")

# 05/06/2021

date_field = driver.find_element_by_id('example-input-date')
date_to_set = datetime(2021, 6, 5)
date_field.send_keys(date_to_set.strftime('%m'))
date_field.send_keys(date_to_set.strftime('%d'))
date_field.send_keys(date_to_set.strftime('%Y'))


# 2012.05.05 05:05:05:555

date_to_set = datetime(2012, 5, 5, 5, 5, 5, 555)
datetime_field = driver.find_element_by_id('example-input-date-time')
insert_date = date_to_set.strftime('%Y-%m-%d %H:%M:%S:%f')
insert_date = insert_date.replace('000', '')
print(insert_date)
datetime_field.send_keys(insert_date)

# 05/12/2000 12:01 PM
# Highly depends on the region and timezon and calendar your browser is using!
date_time_local_field = driver.find_element_by_id('example-input-date-time-local')
date_to_set = datetime(2000, 12, 5, 12, 1)
date_time_local_field.send_keys(date_to_set.strftime('%m'))
date_time_local_field.send_keys(date_to_set.strftime('%d'))
date_time_local_field.send_keys(date_to_set.strftime('%Y'))
date_time_local_field.send_keys("\t")
date_time_local_field.send_keys(date_to_set.strftime('%I')) # because I have US regional settings AM/PM
date_time_local_field.send_keys(date_to_set.strftime('%M'))
date_time_local_field.send_keys(date_to_set.strftime('%p')) # because I have US regional settings AM/PM


# December 1995
# Highly depends on the region and timezon and calendar your browser is using!
month_field = driver.find_element_by_id('example-input-month')
date_to_set = datetime(1995, 12, 1)
month_field.send_keys(date_to_set.strftime('%m'))
month_field.send_keys('\t')
month_field.send_keys(date_to_set.strftime('%Y'))

# Week 52, 2015

week_field = driver.find_element_by_id('example-input-week')
date_to_set = datetime(2015, 12, 28)
week_field.send_keys(date_to_set.strftime('%W'))
week_field.send_keys(date_to_set.strftime('%Y'))

# 12:25 AM
# Highly depends on the region and timezon and calendar your browser is using!
time_field = driver.find_element_by_id('example-input-time')
date_to_set = datetime(2021, 7, 8, 12, 25)
time_field.send_keys(date_to_set.strftime('%I:%M'))
time_field.send_keys(date_to_set.strftime('%p'))
driver.quit()