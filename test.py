
# encoding:utf-8

# import sys
# reload (sys)
# sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pyquery import PyQuery as pq
import time
import webbrowser
#生成html文件
import subprocess
from PIL import Image
from PIL import ImageOps
from selenium import webdriver
import time,os,sys



driver = webdriver.Chrome()
driver.get("https://ccclub.cmbchina.com/mca/MQuery.aspx?WT.refp=%2Fcard-progress$")
url = driver.current_url   
print(url)
cookie = driver.get_cookies()


# for cookie in driver.get_cookies():
#     print(cookie['name'], cookie['value'])

driver.find_element_by_id("txbcardid").send_keys("410721199709154048")
driver.find_element_by_id("tbxExtraCode").send_keys("1234")
text = driver.find_element_by_class_name("new_extraCode").text
html=driver.page_source
d = pq(html)
driver.save_screenshot('screenshot.png')

# 生成html
z = d(".new_extraCode").html()

print(driver.find_element_by_id("extraimg").location)
left = driver.find_element_by_id("extraimg").location['x']
top = driver.find_element_by_id("extraimg").location['y']
right = driver.find_element_by_id("extraimg").location['x'] + driver.find_element_by_id("extraimg").size['width']
bottom = driver.find_element_by_id("extraimg").location['y'] + driver.find_element_by_id("extraimg").size['height']

im = Image.open('screenshot.png') 
im = im.crop((left, top, right, bottom))
im.save('screenshot.png')
    

GEN_HTML = "demo_1.html"  #命名生成的html

f = open(GEN_HTML,'w')
message = """
<html>
<head></head>
<body>
<p>Hello,World!</p>
<p>Add webbrowser function</p>
<div>%s</div>
</body>
</html>"""%(z)

f.write(message)
f.close()

# webbrowser.open(GEN_HTML,new = 1)

# print(text)
#print cookie

# driver.quit()