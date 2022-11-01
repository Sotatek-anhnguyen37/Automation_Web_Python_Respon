import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BaseSetUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        s = Service("C:/Users/admin/Downloads/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")
