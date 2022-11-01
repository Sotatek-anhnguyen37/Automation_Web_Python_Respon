class Product:
    def __init__(self, name, link, price, title):
        self.name = name
        self.link = link
        self.price = price
        self.title = title

    def show(self):
        print("========================================")
        print("Product Name : ", self.name)
        print("Product Link : ", self.link)
        print("Product Price: ", self.price)
        print("Website Name : ", self.title)


