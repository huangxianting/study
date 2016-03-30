#coding=utf-8
__author__ = 'sherry'

from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('level_locate.html')
dr.get(file_path)

#找到Link1按钮并点击
dr.find_element_by_link_text("Link1").click()


#保持鼠标点击悬停
webdriver.ActionChains(dr).click_and_hold(dr.find_element_by_link_text("Action")).perform()



