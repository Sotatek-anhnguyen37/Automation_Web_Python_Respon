from selenium import webdriver
from Pages.AmazonPage import AmazonPage
from selenium.webdriver.chrome.service import Service

import time
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service("C:/Users/admin/Downloads/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()
        cls.driver.get("https://amazon.com")

    def test_login_valid(self):
        driver = self.driver
        amazonpage = AmazonPage(driver)
        amazonpage.enter_name_product()
        amazonpage.click_search_button()
        amazonpage.get_list_product()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")