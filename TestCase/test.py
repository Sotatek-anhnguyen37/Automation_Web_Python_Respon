from operator import attrgetter
from Base.BaseSetUp import BaseSetUp
from Constansts import EndPoint
from Pages.AmazonPage import AmazonPage
from Pages.EbayPage import EbayPage


class LoginTest(BaseSetUp):
    lst = []

    def test_search_product(self):
        driver = self.driver
        self.driver.get(EndPoint.EBAY_LINK)
        ebaypage = EbayPage(driver)
        ebaypage.enter_information_product()
        ebaypage.click_search_button()
        lst = ebaypage.get_list_product()

        self.driver.get(EndPoint.AMAZON_LINK)
        amazonpage = AmazonPage(driver)
        amazonpage.enter_name_product()
        amazonpage.click_search_button()
        lst.extend(amazonpage.get_list_product())

        # lst.sort(key=lambda x: x.price)
        lst.sort(key=attrgetter('price'))
        for i in lst:
            i.show()
