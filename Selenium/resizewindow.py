import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

b = webdriver.Firefox()
b.get('http://wikipedia.org')
time.sleep(2)
b.set_window_size(1024,768)
time.sleep(3)
print(b.get_window_size())
time.sleep(3)
b.maximize_window()
print(b.get_window_size())
time.sleep(8)
b.close()