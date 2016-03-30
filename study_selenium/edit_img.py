# coding=utf-8
__author__ = 'sherry'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Firefox()

url = 'http://gongzuojihui.com/m/login.html'

print('now access', url)
browser.get(url)

# 给用户名的输入框标红
js="var q=document.getElementById(\"loginname\");q.style.border=\"1px solid red\";"
#调用js
browser.execute_script(js)

# 填写合法用户名密码登录
browser.find_element_by_id("loginname").send_keys("18673215474")
browser.find_element_by_id("password").send_keys("123456")
browser.find_element_by_id("loginBtn").click()

# 等待icon-close执行
'''
time.sleep(1)
browser.find_element_by_class_name("icon-close").click()
'''
try:
    icon_close = WebDriverWait(browser,10).until(
        EC.visibility_of_element_located((By.CLASS_NAME,'icon-close'))
    )
    #print dir(icon_close)
    icon_close.click()

finally:
    pass
'''
# 进入用户信息
try:
    header_user = WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.CLASS_NAME,'header-user'))
    )
    #print  dir(element)
    header_user.click()

finally:
    pass

'''
time.sleep(1)
browser.find_element_by_class_name('header-user').click()


# 打开编辑信息页面
time.sleep(1)
browser.switch_to_frame('main')
browser.find_element_by_xpath('//button[@ref-click="editInfo"]').click()

# 打开头像上传页面

#browser.find_element_by_id('uploadImg').send_keys('/Users/sherry/PycharmProjects/1.jpg')
browser.find_element_by_xpath('//input[@type="file"]').send_keys('/Users/sherry/PycharmProjects/1.jpg')
browser.find_element_by_xpath('//button[@ref-click="postInfo"]').click()
