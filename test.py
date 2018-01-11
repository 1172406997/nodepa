
#encoding:utf-8

import sys
reload (sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://ccclub.cmbchina.com/mca/MQuery.aspx?WT.refp=%2Fcard-progress$")

cookie = driver.get_cookies()

for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])

driver.find_element_by_id("txbcardid")

print driver.find_element_by_id("txbcardid")
print cookie

driver.quit()