import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.live_score_page import LiveScoresPage

class TestLiveScoresPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserWrapper()
        options = browser.get_caps()[0]
        cls.driver = browser.get_driver(options)
        cls.live_scores_page = LiveScoresPage(cls.driver)

    def test_live_scores_display(self):
        self.assertTrue(self.live_scores_page.verify_live_score_element_displayed(), "Live scores are not displayed correctly")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
