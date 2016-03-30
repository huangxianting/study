#coding=utf-8
__author__ = 'sherry'

from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('http://baidu.com')
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
time.sleep(2)
browser.find_element_by_xpath('//input[@type="submit"]').click()
time.sleep(2)
browser.back()
browser.find_element_by_link_text("贴吧").click()
