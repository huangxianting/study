# coding:utf-8
__author__ = 'sherry'


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


dr = webdriver.Chrome()

# 打开百度网站并搜索python
dr.get('http://baidu.com')

dr.find_element_by_id('kw').send_keys('python')
dr.find_element_by_id('su').click()

# 页面滚动到底部
js = "document.body.scrollTop=10000"

time.sleep(1)
dr.execute_script(js)
time.sleep(2)

# 页面滚动到顶部
js = "document.body.scrollTop=100"

dr.execute_script(js)

dr.get('http://gongzuojihui.com/m/login.html')

# 填写合法用户名密码登录
dr.find_element_by_id("loginname").send_keys("18673215474")
dr.find_element_by_id("password").send_keys("123456")
dr.find_element_by_id("loginBtn").click()

# 等待icon-close执行
time.sleep(1)
dr.find_element_by_class_name("icon-close").click()

# 进入人才库
time.sleep(1)
dr.switch_to_frame('main')
dr.find_element_by_xpath('//*[@id="professions2"]/a[1]/div').click()

# 滚动人才列表
dr.switch_to_frame('main')
js = 'document.getElementById(\"list\").scrollTop=200'
time.sleep(1)
dr.execute_script(js)