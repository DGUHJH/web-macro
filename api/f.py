# MLB파크

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/Users/hwangjaehyeong/Desktop/utils/chromedriver')
driver.get('https://secure.donga.com/membership/login.php?gourl=http%3A%2F%2Fmlbpark.donga.com%2Fmp')

id_editor = driver.find_element_by_xpath('//*[@name="bid"]')
id_editor.send_keys('nandayo97')

password_editor = driver.find_element_by_xpath('//*[@name="bpw"]')
password_editor.send_keys('dkghdthdud97')

login_button = driver.find_element_by_xpath('//*[@class="btn_process"]')
login_button.click()

time.sleep(2)

driver.get('http://mlbpark.donga.com/mp/b.php?m=write&b=bullpen')

select_category = Select(driver.find_element_by_xpath('//*[@name="category"]'))
select_category.select_by_index(20)

title_editor = driver.find_element_by_xpath('//*[@class="tit_input"]/input[1]')
title_editor.send_keys('123qwe')

