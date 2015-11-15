#coding:utf-8
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

display = Display(visible=0, size=(800, 600))
display.start()
count=0
while count <=20:

        w=webdriver.Firefox()

        w.get('https://cschannel.alipay.com/portal.htm?sourceId=114&enterurl=https://cshall.alipay.com/hall/index.htm')
	w.find_element_by_css_selector("textarea[seed=\"inputField-content\"]").send_keys(u"退款未到帐")
	time.sleep(2)
	w.find_element_by_id("main-submit-btn").click()
	w.find_element_by_css_selector("textarea[seed=\"inputField-content\"]").send_keys(u"退款未到帐")
	time.sleep(2)
	w.find_element_by_id("main-submit-btn").click()
	print "add custom times:",count
	time.sleep(10)
	w.find_element_by_css_selector("a[seed=\"PCportal_self_toYunzaixian\"]").click()
	time.sleep(2)
	w.quit()
	count+=1
	time.sleep(30)


display.stop()
