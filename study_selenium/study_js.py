#coding=utf-8
__author__ = 'sherry'

from selenium import webdriver
import time

dr = webdriver.Firefox()

dr.get('http://www.gongzuojihui.com/m/login.html')

#给用户名的输入框标红
js="var q=document.getElementById(\"loginname\");q.style.border=\"1px solid red\";"
#调用js
dr.execute_script(js)
time.sleep(3)