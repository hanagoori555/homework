import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Check:
    def __init__(self, loc):
        self.loc = loc

    def exist(self, url):
        # url
        driver = webdriver.Chrome()
        driver.get(url)
        #  css
        time.sleep(5)
        input_username = driver.find_element(By.CSS_SELECTOR, self.loc)
        # is
        if input_username is None:
            return 'Элемент не найден'
        else:
            return 'Элемент найден'
