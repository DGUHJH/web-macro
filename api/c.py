# 에펨코리아

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def c(webdriver_url, title, body, image, image2):

  driver = webdriver.Chrome(f'{webdriver_url}')
  driver.get('https://www.fmkorea.com/')

  id_editor = driver.find_element_by_xpath('//*[@name="user_id"]')
  id_editor.send_keys('nandayo97')

  password_editor = driver.find_element_by_xpath('//*[@name="password"]')
  password_editor.send_keys('dkghddl97!!')

  login_submit_button = driver.find_element_by_xpath('//*[@class="li2 mpReset"]/button[1]')
  login_submit_button.click()

  driver.get('https://www.fmkorea.com/index.php?mid=humor&act=dispBoardWrite')

  close_button = driver.find_element_by_xpath('//*[@class="btn_img"]')
  close_button.click()

  select_category = Select(driver.find_element_by_xpath('//*[@name="category_srl"]'))
  select_category.select_by_index(1)

  title_editor = driver.find_element_by_xpath('//*[@name="title"]')
  title_editor.send_keys(f'{title}')

  driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="input_area xpress_xeditor_editing_area_container"]/iframe[1]'))

  write_body_editor = driver.find_element_by_xpath('//html/body')
  write_body_editor.click()

  write_body_editor = driver.find_element_by_xpath('//html/body')
  write_body_editor.send_keys(f'{body}')

  driver.switch_to.default_content()

  file_upload_editor = driver.find_element_by_xpath('//*[@id="xe-fileupload"]')
  file_upload_editor.send_keys(f'{image}')
  if image2 != '':
    time.sleep(10)
    file_upload_editor = driver.find_element_by_xpath('//*[@id="xe-fileupload"]')
    file_upload_editor.send_keys(f'{image2}')

  time.sleep(10)

  submit_button = driver.find_element_by_xpath('//*[@class="bd_btn blue"]')
  submit_button.click()

  time.sleep(10)

  driver.quit()