# 개그집합소

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def g(webdriver_url, title, body, image, image2):

  driver = webdriver.Chrome(f'{webdriver_url}')
  driver.get('https://gezip.net/')

  id_editor = driver.find_element_by_xpath('//*[@name="mb_id"]')
  id_editor.send_keys('nighttear')

  password_editor = driver.find_element_by_xpath('//*[@name="mb_password"]')
  password_editor.send_keys('Elthtm2019!')

  login_button = driver.find_element_by_xpath('//*[@class="btn btn-navy btn-block en"]')
  login_button.click()

  driver.get('https://gezip.net/bbs/write.php?bo_table=humor2')

  title_editor = driver.find_element_by_xpath('//*[@name="wr_subject"]')
  title_editor.send_keys(f'{title}')

  driver.switch_to.frame(driver.find_element_by_xpath('//*[@src="https://gezip.net/plugin/editor/smarteditor2/SmartEditor2Skin.html"]'))
  driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="se2_input_wysiwyg"]'))

  write_body_editor = driver.find_element_by_xpath('//html/body')
  write_body_editor.send_keys(f'{body}')

  driver.switch_to.default_content()

  driver.switch_to.frame(driver.find_element_by_xpath('//*[@src="https://gezip.net/plugin/editor/smarteditor2/SmartEditor2Skin.html"]'))
  image_editor = driver.find_element_by_xpath('//*[@class="se2_photo ico_btn"]')
  image_editor.click()

  driver.switch_to.window(driver.window_handles[1])

  image_editor_upload = driver.find_element_by_xpath('//*[@id="fileupload"]')
  image_editor_upload.send_keys(f'{image}')
  if image2 != '':
    image_editor_upload.send_keys(f'{image2}')

  time.sleep(10)

  image_submit_button = driver.find_element_by_xpath('//*[@id="img_upload_submit"]')
  image_submit_button.click()

  driver.switch_to.window(driver.window_handles[0])

  submit_button = driver.find_element_by_xpath('//*[@id="btn_submit"]')
  submit_button.click()

  time.sleep(10)

  driver.quit()