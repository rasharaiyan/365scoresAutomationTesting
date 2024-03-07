from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class SearchTesting(BasePage):
    search_input = "main - header - module - mobile - input"

    def __init__(self, driver):
        super().__init__(driver)
        self.init_page()

    def init_page(self):
        self.search_INPUT = self.driver.find_element(By.CLASS_NAME, "main-header-module-mobile-input")

    def fill_txt_in_search(self):
        self.search_INPUT.send_keys("Real Madrid")

    def enter_search(self):
        self.search_INPUT.submit()

    def perform_search(self):
        self.fill_txt_in_search()
        self.enter_search()