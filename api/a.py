# 뽐뿌

# 카테고리 설정 - 유머이미지 / 기타

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def a(webdriver_url, title, body, image):

  driver = webdriver.Chrome(f'{webdriver_url}')
  driver.get('https://www.ppomppu.co.kr/')

  login_link_button = driver.find_element_by_xpath('//*[@class="login_box"]/p/a')
  login_link_button.click()

  id_editor = driver.find_element_by_xpath('//*[@id="user_id"]')
  id_editor.send_keys('nandayo97')

  password_editor = driver.find_element_by_xpath('//*[@id="password"]')
  password_editor.send_keys('dkghddl97!!')

  login_submit_button = driver.find_element_by_xpath('//*[@class="log_btn"]')
  login_submit_button.click()

  driver.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=humor')

  write_link_button = driver.find_element_by_xpath('//*[@class="write_add"]')
  write_link_button.click()

  select_category = Select(driver.find_element_by_xpath('//select[@name="category"]'))
  select_category.select_by_index(1)

  write_title_editor = driver.find_element_by_xpath('//*[@class="top_inp title"]')
  write_title_editor.send_keys(f'{title}')

  write_link_editor = driver.find_element_by_xpath('//*[@class="top_inp link"]')
  write_link_editor.send_keys('')

  write_sub_body = driver.find_element_by_xpath('//*[@class="cheditor-editarea"]')
  write_sub_body.click()

  driver.switch_to.frame(driver.find_element_by_css_selector('iframe'))

  write_body_editor = driver.find_element_by_xpath('//html/body')
  write_body_editor.send_keys(f'{body}')

  driver.switch_to.default_content()

  write_sub_body = driver.find_element_by_xpath('//*[@class="btn btn-image-upload"]')
  write_sub_body.click()
  time.sleep(1)

  driver.switch_to.frame(driver.find_element_by_css_selector('iframe'))

  file_upload_editor = driver.find_element_by_xpath('//*[@id="inputImageUpload"]')
  file_upload_editor.send_keys(f'{image}')

  file_upload_editor_button = driver.find_element_by_xpath('//*[@id="buttonWrapper"]/img[1]')

  time.sleep(10)

  file_upload_editor_button.click()

  driver.switch_to.default_content()

  submit_button = driver.find_element_by_xpath('//*[@id="ok_button"]')
  submit_button.click()

  time.sleep(10)

  driver.quit()