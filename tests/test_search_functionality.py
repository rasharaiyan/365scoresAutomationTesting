import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.search_functionality import SearchTesting

class TestSearchFunctionality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserWrapper()
        options = browser.get_caps()[0]
        cls.driver = browser.get_driver(options)
        cls.search_page = SearchTesting(cls.driver)

    def test_search(self):
        self.search_page.perform_search()
        time.sleep(5)
        self.assertIn("Real Madrid", self.search_page.get_url_driver(), "Search did not work as expected")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
