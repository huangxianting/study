# coding:utf8
__author__ = 'sherry'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

dr = webdriver.Firefox()

dr.get('file:///Users/sherry/PycharmProjects/drop_down.html')

m = dr.find_element_by_id('ShippingMethod')
time.sleep(2)
m.find_element_by_xpath('//option[@value="11.61"]').click()
time.sleep(2)