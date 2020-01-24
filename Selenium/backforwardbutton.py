from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

b = webdriver.Firefox()
b.get('http://google.com')

elem = b.find_element_by_link_text('Imagens')
time.sleep(3)
elem.click()
time.sleep(4)
b.back()
time.sleep(6)
b.close()