# coding:utf-8
__author__ = 'sherry'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get('http://www.gongzuojihui.com/m/#myJob')

driver.find_element_by_id('loginname').send_keys('18673215474')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('loginBtn').click()

# 等待icon-close执行

try:
    icon_close = WebDriverWait(driver,5).until(
        EC.visibility_of_element_located((By.CLASS_NAME,'icon-close'))
    )
    # print dir(icon_close)
    icon_close.click()

finally:
    pass

#driver.get('http://www.gongzuojihui.com/m/#myJob')

'''
try:
    my_job = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.XPATH,'//a[@hash="myJob"]'))
    )
    # print dir(my_job)
    my_job.click()
finally:
    pass
'''
time.sleep(2)
driver.find_element_by_xpath('//a[@hash="myJob"]').click()

time.sleep(0.5)
driver.switch_to_frame('main')
driver.find_element_by_xpath('//span[@class="icon-add"]').click()

time.sleep(2)

'''
# 将鼠标移动到职位类别一栏上方
m = driver.find_element_by_xpath('//*[@id="categoryInput"]/div/div')
webdriver.ActionChains(driver).move_to_element(m).perform()

# 选择IOS工程师
time.sleep(1)
driver.find_element_by_xpath('//*[@id="categoryInput"]/div/div/div[2]/ul/li[2]').click()
'''
m = driver.find_element_by_xpath('//*[@id="categoryInput"]/div/div/div[2]/ul')
m.find_element_by_xpath('//*[@id="categoryInput"]/div/div/div[2]/ul/li[2]').click()
