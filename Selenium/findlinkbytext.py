from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://google.com')

try:
    driver.find_element_by_link_text('')
    print('Test Pass: Element found by link text')

except Exception as e:
    print('Exception found', format(e))

driver.close()