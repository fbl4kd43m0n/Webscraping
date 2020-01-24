import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.witzler.com.br')

ids = driver.find_elements_by_xpath('//*[@href]')

for ii in ids:
    print(ii.get_attribute('href'))

time.sleep(4)
driver.close()