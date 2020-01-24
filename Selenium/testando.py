import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://en.wikipedia.org')
print(driver.title)
time.sleep(8)
driver.quit()