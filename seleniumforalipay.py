#coding:utf-8
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import random

display = Display(visible=0, size=(800, 600))
display.start()
count=0
pool=[u"淘宝退款没到帐",u"花呗怎么还款",u"付款成功交易失败",u"退款没到帐",u"花呗账单查询",u"花呗怎么还款",u"钱没了"\
,u"退款没收到",u"退款查不到",u"花呗还款额度没有恢复",u"花呗不能开通",u"退款没退给我",u"预留手机号不一致",u"怎么申请退款"]
while count <=50:
	try:
		w=webdriver.Firefox()
		w.get('https://cschannel.alipay.com/portal.htm?sourceId=114&enterurl=https://cshall.alipay.com/hall/index.htm')
		w.find_element_by_css_selector("textarea[seed=\"inputField-content\"]").send_keys(u"淘宝退款没到帐")
		time.sleep(2)
		w.find_element_by_id("main-submit-btn").click()
		ask=pool[random.randint(0,13)]
		w.find_element_by_css_selector("textarea[seed=\"inputField-content\"]").send_keys(ask)
		time.sleep(2)
		w.find_element_by_id("main-submit-btn").click()
		print ask,count
		time.sleep(10)
		w.find_element_by_css_selector("a[seed=\"PCportal_self_toYunzaixian\"]").click()
		time.sleep(2)
		w.quit()
		count+=1
		time.sleep(30)
	except:
		print "a error have raiseup,please check the log"
		try:
			w.quit()
		except:
			pass
		display.stop()

display.stop()
