from selenium import webdriver

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'gLFyf' # name
        self.btn_search = '/html/body/div/div[4]/form/div[2]/div[1]/div[3]/center/input[1]' # xpath
        self.btn_lucky = '/html/body/div/div[4]/form/div[2]/div[1]/div[3]/center/input[2]' # xpath

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_class_name(self.search_bar).send_keys(word)
        self.driver.find_element_by_xpath(self.btn_search).click()

    def lucky(self, word='None'):
        self.driver.find_element_by_class_name(self.search_bar).send_keys(word)
        self.driver.find_element_by_xpath(self.btn_lucky).click()
        

ff = webdriver.Firefox()
g = Google(ff)
g.navigate()
#g.search('Live de Python')
g.lucky('Piura')
g.quit()

#bar = ff.find_element_by_class_name('gLFyf')
#bar.send_keys('Live de python')