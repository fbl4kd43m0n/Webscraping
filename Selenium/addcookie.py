from selenium import webdriver

d = webdriver.Firefox()
d.get('http://bing.com')

cookie={'fruit':'mango','chocolate':'milk'}
d.add_cookie(cookie)

print(d.get_cookies())

#d.close()