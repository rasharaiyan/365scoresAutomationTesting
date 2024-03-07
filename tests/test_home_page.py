import unittest
from selenium import webdriver
from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage

class TestHomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserWrapper()
        options = browser.get_caps()[0]
        cls.driver = browser.get_driver(options)
        cls.home_page = HomePage(cls.driver)

    def test_home_page_load(self):
        self.assertIn("365scores.com", self.home_page.home_page_load(), "Home page did not load correctly")

    def test_navigate_to_football(self):
        wait = WebDriverWait(self.driver, 10)
        football_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/header/div/div/div[1]/div[1]/div[3]/div/div/span/div")))
        football_link.click()

    def test_search_functionality(self):
        self.home_page.search_functionality()
        time.sleep(5)
        self.assertIn("Real Madrid", self.home_page.get_url_driver(), "Search functionality did not work as expected")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
