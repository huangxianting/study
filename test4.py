#coding=utf-8
__author__ = 'sherry'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

dr = webdriver.Chrome()

dr.get('http://baidu.com')

dr.find_element_by_id('kw').send_keys('Python')
time.sleep(2)
dr.find_element_by_id('kw').clear()
time.sleep(1)

dr.find_element_by_id('su').submit()

print dr.find_element_by_id('cp').text