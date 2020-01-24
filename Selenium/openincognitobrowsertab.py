from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://bing.com')