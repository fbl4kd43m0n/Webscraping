from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://google.com')

id = driver.find_elements_by_xpath('//*[@class]')

for ii in id:
    print(ii.get_attribute('class'))

driver.close()