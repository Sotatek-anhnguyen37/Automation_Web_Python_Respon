class Product:
    def __init__(self, name, link, price):
        self.name = name
        self.link = link
        self.price = price

    def getName(self):
        return self.name

    def getLink(self):
        return self.link

    def getPrice(self):
        return self.price

    def setName(self, name):
        self.name = name

    def setLink(self, link):
        self.link = link

    def setNPrice(self, price):
        self.price = price
