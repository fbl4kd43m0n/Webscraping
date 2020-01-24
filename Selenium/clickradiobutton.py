import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

b = webdriver.Firefox()
b.get('http://www.zkoss.org/zkdemo/input/radio_button')

for i in b.find_elements_by_xpath("//*[@type='radio']"):
    i.click()

time.sleep(6)
b.close()