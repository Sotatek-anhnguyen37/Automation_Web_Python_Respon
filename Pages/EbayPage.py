from selenium import webdriver
from selenium.webdriver.common.by import By

from Object.Product import Product


class EbayPage():
    def __init__(self, driver):
        self.driver = driver
        self.search_textbox_id = "gh-ac"
        self.search_button_id = "gh-btn"
        self.list_product_xpath = "//div[@id='srp-river-results']//div[@class='s-item__wrapper clearfix']"

    def enter_information_product(self):
        self.driver.find_element(By.ID, self.search_textbox_id).send_keys("iphone")

    def click_search_button(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

    def get_list_product(self):
        lst = []
        title = self.driver.title.replace("iphone | ", "")
        list_product = self.driver.find_elements(By.XPATH, self.list_product_xpath)
        print(list_product)
        for items in list_product:
            name = items.find_element(By.XPATH, ".//div[@class='s-item__info clearfix']//span[@role='heading']").text
            price = items.find_element(By.XPATH, ".//div[@class='s-item__info clearfix']//span[@class='s-item__price']").text.replace(" VND",  "").replace(",", "")
            if "Apple iPhone 11" in name and "to" not in price:
                link = items.find_element(By.XPATH,
                                          ".//div[@class='s-item__info clearfix']//a[@class='s-item__link']").get_attribute(
                    "href")
                pro = Product(name, link, float(price), title)
                lst.append(pro)
        return lst