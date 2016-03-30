#-*-coding=utf-8

from selenium import webdriver
from selenium.webdriver.common import alert
import os,time

driver= webdriver.Chrome()

driver.get("http://www.baidu.com")


#进入搜索设置页

driver.find_element_by_link_text('设置').click()
time.sleep(0.5)
driver.find_element_by_link_text("搜索设置").click()


#设置每页搜索结果为50条
time.sleep(1)

m=driver.find_element_by_name("NR")

m.find_element_by_xpath("//*[@id='nr']/option[3]").click()



#保存设置的信息

driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()

driver.switchTo().alert()
alert.Alert.accept()
#driver.switch_to_alert().accept()


#跳转到百度首页后，进行搜索表（一页应该显示50条结果）

driver.find_element_by_id("kw").send_keys("selenium")

driver.find_element_by_id("su").click()

time.sleep(3)
