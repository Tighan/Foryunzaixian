#coding:utf-8
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

display = Display(visible=0, size=(800, 600))
display.start()

w=webdriver.Firefox()
w.get('https://cschannel.alipay.com/portal.htm?sourceId=114&enterurl=https://cshall.alipay.com/hall/index.htm')
w.find_element_by_css_selector("textarea[seed=\"inputField-content\"]").send_keys(u"退款未到帐")
time.sleep(2)
w.find_element_by_id("main-submit-btn").click()
w.find_element_by_css_selector("textarea[seed=\"inputField-content\"]").send_keys(u"退款未到帐")
time.sleep(2)
w.find_element_by_id("main-submit-btn").click()
time.sleep(10)
w.find_element_by_css_selector("a[seed=\"PCportal_self_toYunzaixian\"]").click()
time.sleep(2)
num=w.find_elements_by_css_selector("div[class=\"content\"]")[4].text
print num
w.quit()


display.stop()
