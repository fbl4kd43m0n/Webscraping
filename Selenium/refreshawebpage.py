import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d = webdriver.Firefox()
d.get('http://wikipedia.org')

time.sleep(3)
d.refresh()
time.sleep(2)
d.close()
