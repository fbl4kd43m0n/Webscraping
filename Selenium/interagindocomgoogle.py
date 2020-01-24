import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://google.com')

search = browser.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input')
search.send_keys('Python 3')
search.send_keys(Keys.RETURN)
time.sleep(6)
search.clear()
time.sleep(2)
browser.close()