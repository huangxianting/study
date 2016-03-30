#coding=utf-8
__author__ = 'sherry'

from selenium import webdriver
import time

browser = webdriver.Firefox()

file_path = 'file:///Users/sherry/PycharmProjects/frame.html'

browser.get(file_path)
browser.maximize_window()

browser.implicitly_wait(30)
browser.switch_to_frame('f1')
browser.switch_to_frame('f2')