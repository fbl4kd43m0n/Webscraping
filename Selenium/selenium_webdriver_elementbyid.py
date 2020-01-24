from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://google.com')

try:
    driver.find_elements_by_class_name('gb_g')
    print('Test pass: Class found')

except Exception as e:
    print('Exception found', format(e))

driver.close()