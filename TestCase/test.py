from selenium import webdriver

from Object.Product import Product
from Pages.AmazonPage import AmazonPage
from selenium.webdriver.chrome.service import Service

import time
import unittest

from Pages.EbayPage import EbayPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service("C:/Users/admin/Downloads/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()

    def take_second(elem):
        return elem[1]
    def test_search_product(self):
        driver = self.driver
        lst = []
        self.driver.get("https://www.ebay.com/")
        ebaypage = EbayPage(driver)
        ebaypage.enter_information_product()
        ebaypage.click_search_button()
        lst = ebaypage.get_list_product()

        self.driver.get("https://amazon.com")
        amazonpage = AmazonPage(driver)
        amazonpage.enter_name_product()
        amazonpage.click_search_button()
        lst.extend(amazonpage.get_list_product())

        sorted_list = sorted(lst, key=self.take_second)
        for i in sorted_list:
            i.show()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")
