class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def clickElement(self, element):
        element.click()

    def senKeyElement(self, element, key):
        element.send_keys(key)
