import time
from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy_type',1)
profile.set_preference('network.proxy.http',"124.40.251.146")
profile.set_preference('network.proxy.http_port',3128)
profile.update_preferences()

d = webdriver.Firefox(firefox_profile=profile)
d.get('http://whatismyipaddress.com')
time.sleep(3)
d.close()