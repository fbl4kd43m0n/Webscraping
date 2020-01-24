from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.get('http://www.airindia.in/contact-details.htm')

doc = driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for email in emails:
    print(email)
