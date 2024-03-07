import unittest
from datetime import time
import time
from telnetlib import EC
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from pip._internal.utils import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from infra.base_page import BasePage

logger = logging.getLogger('selenium')

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def home_page_load(self):
        return self.driver.current_url
    def navigate_to_football(self):
        football_link = self.driver.find_element_by_xpath("/html/body/div[2]/div/header/div/div/div[1]/div[1]/div[3]/div/div/span/div")
        football_link.click()

    def search_functionality(self):
        search_box = self.driver.find_element(By.CLASS_NAME,"main-header-module-mobile-buttons-search-icon")
        search_box.send_keys("Real Madrid")
        search_box.submit()