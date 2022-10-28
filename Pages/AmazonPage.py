from selenium.webdriver.common.by import By


class AmazonPage():
    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_id = "twotabsearchtextbox"
        self.search_button_xpath = "//*[@id='nav-search-submit-button']"
        self.list_product_xpath = "//div[@class='s-main-slot s-result-list s-search-results sg-row']//div[" \
                                  "@class='a-section'] "

    def enter_name_product(self):
        self.driver.find_element(By.ID, self.search_textbox_id).send_keys("iphone")

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def get_list_product(self):
        list_product = self.driver.find_elements(By.XPATH, "//div[@class='s-main-slot s-result-list s-search-results "
                                                           "sg-row']//div[@class='s-card-container s-overflow-hidden "
                                                           "aok-relative puis-include-content-margin puis "
                                                           "s-latency-cf-section s-card-border']")

        for items2 in list_product:
            name = items2.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
            if "iPhone 11" in name.text:

                link = items2.find_element(By.XPATH,
                                           ".//a[@class='a-link-normal s-underline-text s-underline-link-text "
                                           "s-link-style a-text-normal']").get_attribute('href')
                price = items2.find_element(By.XPATH, ".//span[@class='a-price-whole']")
                print(name.text)
                print(link)
                print(price.text)
                print("====================")
