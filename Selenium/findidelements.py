from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://studiohackingx.com')

ids = driver.find_elements_by_xpath('//*[@id]')

for ii in ids:
    print(ii.get_attribute('id'))

driver.close