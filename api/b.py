# 보배드림

import time
from selenium import webdriver

def b(webdriver_url, title, body, image, image2):

  driver = webdriver.Chrome(f'{webdriver_url}')
  driver.get('https://security.bobaedream.co.kr/member/slogin.php')

  id_editor = driver.find_element_by_xpath('//*[@id="id"]')
  id_editor.send_keys('nandayo97')

  password_editor = driver.find_element_by_xpath('//*[@id="pw"]')
  password_editor.send_keys('dkghddl97!!')

  login_submit_button = driver.find_element_by_xpath('//*[@class="btn_login"]/button[1]')
  login_submit_button.click()

  driver.get('https://www.bobaedream.co.kr/board/bulletin/write?code=strange')

  write_title_editor = driver.find_element_by_xpath('//*[@class="input01"]')
  write_title_editor.send_keys(f'{title}')

  driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="cheditor-editarea"]'))

  write_body_editor = driver.find_element_by_xpath('//html/body')
  write_body_editor.click()

  write_body_editor = driver.find_element_by_xpath('//html/body')
  write_body_editor.send_keys(f'{body}')

  driver.switch_to.default_content()

  write_sub_body = driver.find_element_by_xpath('//*[@class="cheditor-tb-icon36"]')
  write_sub_body.click()
  time.sleep(1)

  driver.switch_to.frame(driver.find_element_by_css_selector('iframe'))

  file_upload_editor = driver.find_element_by_xpath('//*[@id="inputImageUpload"]')
  file_upload_editor.send_keys(f'{image}')
  if image2 != '':
    file_upload_editor.send_keys(f'{image2}')


  file_upload_editor_button = driver.find_element_by_xpath('//*[@id="buttonWrapper"]/img[1]')

  time.sleep(10)

  file_upload_editor_button.click()

  driver.switch_to.default_content()

  submit_button = driver.find_element_by_xpath('//*[@class="bot_btn_center"]/a[1]')
  submit_button.click()

  time.sleep(10)

  driver.quit()