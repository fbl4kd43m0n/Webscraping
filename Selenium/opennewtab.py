from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

d = webdriver.Firefox()
d.get('http://google.com')

elm = d.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')