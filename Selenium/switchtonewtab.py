import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d = webdriver.Firefox()
d.get('http://google.com')

body = d.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
d.get('http://bing.com')
time.sleep(3)

d.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.PAGE_UP)
time.sleep(2)

d.find_element_by_tag_name(body).send_keys(Keys.CONTROL+'W')