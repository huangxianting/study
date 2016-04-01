# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

__author__ = 'sherry'

profile = '/Users/sherry/Library/Application Support/Firefox/Profiles/pxy8i4d6.selenium'

foxprofile = webdriver.FirefoxProfile(profile)
time.sleep(1)
browser = webdriver.Firefox(foxprofile)
browser.implicitly_wait(5)
url = 'http://gongzuojihui.com/m/login.html'
browser.get(url)
browser.maximize_window()

# 给用户名的输入框标红
js = "var q=document.getElementById(\"loginname\");q.style.border=\"1px solid red\";"
# 调用js
browser.execute_script(js)

# 填写合法用户名密码登录
browser.find_element_by_id("loginname").send_keys("18673215474")
browser.find_element_by_id("password").send_keys("123456")
browser.find_element_by_id("loginBtn").click()

# 等待icon-close执行

# time.sleep(1)
# browser.find_element_by_class_name("icon-close").click()

try:
    icon_close = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'icon-close'))
    )
    # print dir(icon_close)
    icon_close.click()

finally:
    pass

# # 进入资料页面
# try:
#     header_user = WebDriverWait(browser,10).until(
#         EC.element_to_be_clickable((By.CLASS_NAME,'header-user'))
#     )
#     #print  dir(element)
#     header_user.click()
#
# finally:
#     pass

# 进入资料页面
time.sleep(1)
browser.find_element_by_class_name('header-user').click()

# 打开编辑信息页面
time.sleep(0.5)
browser.switch_to_frame('main')
browser.find_element_by_xpath('//button[@ref-click="editInfo"]').click()

# 修改头像
time.sleep(1)
# browser.find_element_by_id('uploadImg').send_keys('/Users/sherry/PycharmProjects/1.jpg')
browser.find_element_by_xpath('//input[@type="file"]').send_keys('/Users/sherry/PycharmProjects/study_selenium/1.jpg')

# 修改用户名
time.sleep(1)
name = random.choice(['杨朝来', '刘小梅', '刘俊鸣', '陈丹青'])
name = name.decode('utf-8')
nick_name = browser.find_element_by_xpath('//input[@name="nickName"]')
nick_name.clear()
nick_name.send_keys(name)
# print name

# 修改职务
time.sleep(1)
title_name = random.choice(['运营总监', 'CTO', 'CEO', '技术总监', 'HR'])
title_name = title_name.decode('utf-8')
title_name2 = browser.find_element_by_xpath('//input[@name="title"]')
title_name2.clear()
title_name2.send_keys(title_name)
# print title_name

# 随机修改学历
time.sleep(1)
move_degree = browser.find_element_by_xpath('//div[@type="degree"]')
webdriver.ActionChains(browser).move_to_element(move_degree).perform()

value_degree = random.choice(['1', '2', '3', '4', '0'])
ci = 'li[value=\"%s\"]' % value_degree
# print '学历：' + value_degree
time.sleep(1)
browser.find_element_by_css_selector(ci).click()

# 移动鼠标
post_info = browser.find_element_by_xpath('//button[@ref-click="postInfo"]')
webdriver.ActionChains(browser).move_to_element(post_info).perform()
time.sleep(1)

# 随机修改行业经验
move_seniority = browser.find_element_by_xpath('//*[@id="seniorityInput"]/div/div/div[1]')
webdriver.ActionChains(browser).move_to_element(move_seniority).perform()

value_seniority = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '100'])
set_seniority = '//*[@id="seniorityInput"]/div/div/div[2]/ul/li[%s]' % value_seniority
# print '经验：' + value_seniority
# print set_seniority

time.sleep(1)
browser.find_element_by_xpath(set_seniority).click()


# 删除技能标签
while 1:
    try:
        browser.find_element_by_css_selector("span.icon-close").click()
        time.sleep(0.5)
    except NoSuchElementException:
        break
    except:
        s = sys.exc_info()
    #     print("error %s on line %d" % (s[1], s[2].tb_lineno))

# 添加技能标签

tag = browser.find_element_by_css_selector("input.wishTagsInput")
tag.clear()
tag.send_keys("Java")
tag.send_keys(Keys.ENTER)


# 保存
time.sleep(0.5)
post_info.click()

time.sleep(2)

name_status = browser.find_element_by_xpath('//*[@id="rightContent"]/div/table/tbody/tr[2]/td[2]').text == name


def check_status():
    if name_status:
        print('名称修改成功')
    else:
        print('名称修改失败')


check_status()

browser.quit()
