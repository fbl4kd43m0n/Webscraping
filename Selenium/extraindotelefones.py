from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.get('')

doc = driver.page_source

phones = re.findall(r'[(][\d]{3}[)][]?[\d]{3}-[\d]{4}', doc)

for phone in phones:
    print(phone)