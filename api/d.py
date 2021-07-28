# 루리웹

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def d(webdriver_url, title, body, image):

  driver = webdriver.Chrome(f'{webdriver_url}')
  driver.get('https://user.ruliweb.com/member/login')

  id_editor = driver.find_element_by_xpath('//*[@name="user_id"]')
  id_editor.send_keys('realahong97')

  password_editor = driver.find_element_by_xpath('//*[@name="user_pw"]')
  password_editor.send_keys('dkghddl97!!')

  login_button = driver.find_element_by_xpath('//*[@name="login_submit"]')
  login_button.click()

  driver.get('https://bbs.ruliweb.com/community/board/300143/write')

  title_editor = driver.find_element_by_xpath('//*[@class="subject_wrapper col col_10"]/input[1]')
  title_editor.send_keys(f'{title}')

  write_sub_body = driver.find_element_by_xpath('//*[@class="cheditor-tb-icon36"]')
  write_sub_body.click()
  time.sleep(1)

  driver.switch_to.frame(driver.find_element_by_css_selector('iframe'))

  file_upload_editor = driver.find_element_by_xpath('//*[@name="imageUpload[]"]')
  file_upload_editor.send_keys(f'{image}')

  time.sleep(10)

  file_upload_editor_button = driver.find_element_by_xpath('//*[@id="buttonWrapper"]/img[1]')
  file_upload_editor_button.click()

  driver.switch_to.default_content()

  driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="cheditor-editarea"]'))

  write_body_editor = driver.find_element_by_xpath('//html/body')
  write_body_editor.send_keys(f'{body}')

  driver.switch_to.default_content()

  submit_button = driver.find_element_by_xpath('//*[@id="write_submit"]')
  submit_button.click()

  time.sleep(10)

  driver.quit()