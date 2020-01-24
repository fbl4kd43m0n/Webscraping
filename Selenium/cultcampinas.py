from selenium import webdriver

class Cult:
    def __init__(self, driver):
        self.driver = driver
        self.url ='https://www.cultcampinas.com.br'

    def navigate(self):
        self.driver.get(self.url)
