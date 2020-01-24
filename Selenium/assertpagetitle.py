from selenium import webdriver

b = webdriver.Firefox()
b.get('http://google.com')

try:
    assert 'Google' in b.title
    print('Assetion test pass')

except Exception as e:
    print('Assetion test failed', format(e))

b.close()