#coding=utf-8
__author__ = 'sherry'

from selenium import webdriver
import time

brower = webdriver.Chrome()

#访问百度首页

first_url = "http://baidu.com"
print("now access %s") %(first_url)
brower.get(first_url)
time.sleep(2)

#访问百度新闻

second_url = 'http://news.baidu.com'
print("now access %s") %second_url
brower.get(second_url)
time.sleep(2)

brower.back()
print(brower.title)
time.sleep(1)

brower.forward()
print(brower.title)
time.sleep(1)