from selenium import webdriver
import time

b = webdriver.Firefox()
b.get('http://bing.com')

print('Firefox Driver Version: ' + b.capabilities['browserVersion'])
time.sleep(3)
b.close()