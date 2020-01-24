from selenium import webdriver

b = webdriver.Firefox()
b.get('http://studiohackingx.com')

html_source = b.page_source
print(html_source)