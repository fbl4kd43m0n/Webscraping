import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

b = webdriver.Firefox()
b.get('http://demos.dojotoolkit.org/dijit/tests/form/test_CheckBox.html')

for i in range(20):
    try:
        b.find_element_by_xpath(".//*[contains(text(),'cb7: normal checkbox')]").click()
        break
    except NoSuchElementException as e:
        print("retry")
        time.sleep(1)

else:
    print('Test Failed')

b.close()