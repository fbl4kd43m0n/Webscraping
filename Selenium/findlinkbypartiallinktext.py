from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.wikipedia.org/')

try:
    driver.find_element_by_partial_link_text('Terms')
    print('Test pass: Partial link text found')

except Exception as e:
    print('Exception', format(e))

driver.close