from selenium import webdriver
from selenium.webdriver.common.keys import Keys

b = webdriver.Firefox()
b.get('http://wikipedia.org')

elm = b.find_element_by_xpath('/html/body/div[6]/div[3]/div[7]/a/div[2]/span[1]')
elm.click()
print(b.current_url)