# 포모스 - 실패

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/Users/hwangjaehyeong/Desktop/utils/chromedriver')
driver.get('https://www.fomos.kr/login/?done=%2F')

id_editor = driver.find_element_by_xpath('//*[@name="user_id"]')
id_editor.send_keys('nandayo97')

password_editor = driver.find_element_by_xpath('//*[@name="user_pwd"]')
password_editor.send_keys('dkghddl97')

login_button = driver.find_element_by_xpath('//*[@class="login_data"]/tbody/tr/td[2]/input[1]')
login_button.click()

driver.get('https://www.fomos.kr/talk/article_create?bbs_id=3&lurl=%2Ftalk%2Farticle_list%3Fbbs_id%3D3')

title_editor = driver.find_element_by_xpath('//*[@name="title"]')
title_editor.send_keys('asfdsdf')

image_button = driver.find_element_by_xpath('//*[@id="cke_24"]')
image_button.click()

image_upload_button = driver.find_element_by_xpath('//*[@id="cke_Upload_103"]')
image_upload_button.click()



time.sleep(5)