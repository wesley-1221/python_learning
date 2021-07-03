# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月05日
"""

# http://pic.netbian.com/4kdongman/index_6.html

from selenium import webdriver
from selenium.webdriver import ActionChains
from lxml import etree
import time
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('http://pic.netbian.com/4kdongman/')
bro.find_element_by_xpath('//*[@id="main"]/div[2]/a[2]').click()
time.sleep(3)
# page_text = bro.page_source
# print(page_text)
# tree = etree.HTML(page_text)
# print(tree)
time.sleep(3)
bro.quit()

