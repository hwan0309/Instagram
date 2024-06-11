from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://instagram.com')

time.sleep(2)
user_id = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
user_id.click()
user_id.send_keys('hwan_gram')

user_pwd = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
user_pwd.click()
user_pwd.send_keys('wlghks9703!')
user_pwd.click()


#e.send_keys(Keys.ENTER)



# time.sleep(2)
# e = driver.find_element_by_css_selector('input[name="username"]').text
# print(e)

