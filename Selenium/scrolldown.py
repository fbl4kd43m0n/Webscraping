from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

b = webdriver.Firefox()
b.get('http://www.studiohackingx.com')
elm = b.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(8)
elm.send_keys(Keys.HOME)
b.close()