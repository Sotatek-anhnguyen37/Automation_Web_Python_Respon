from selenium.webdriver.common.by import By

from Base.BasePage import BasePage
from Object.Product import Product


class AmazonPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_id = "twotabsearchtextbox"
        self.search_button_xpath = "//*[@id='nav-search-submit-button']"
        self.list_product_xpath = "//div[@class='s-main-slot s-result-list s-search-results sg-row']//div[" \
                                  "@class='a-section'] "

    def enter_name_product(self):
        self.senKeyElement(self.driver.find_element(By.ID, self.search_textbox_id), "iphone")

    def click_search_button(self):
        self.clickElement(self.driver.find_element(By.XPATH, self.search_button_xpath))

    def get_list_product(self):
        lst = []
        title = self.driver.title.replace(" : iphone", "")
        list_product = self.driver.find_elements(By.XPATH, "//div[@class='s-main-slot s-result-list s-search-results "
                                                           "sg-row']//div[@class='s-card-container s-overflow-hidden "
                                                           "aok-relative puis-include-content-margin puis "
                                                           "s-latency-cf-section s-card-border']")

        for items2 in list_product:
            name = items2.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text
            if "iPhone 11" in name:
                link = items2.find_element(By.XPATH,
                                           ".//a[@class='a-link-normal s-underline-text s-underline-link-text "
                                           "s-link-style a-text-normal']").get_attribute('href')
                price = float(items2.find_element(By.XPATH, ".//span[@class='a-price-whole']").text)
                pro = Product(name, link, price*23000, title)
                lst.append(pro)
        return lst
