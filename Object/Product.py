class Product:
    def __init__(self, name, link, price):
        self.name = name
        self.link = link
        self.price = price

    def show(self):
        print("========================================")
        print("Product Name: ", self.name)
        print("Product Link: ", self.link)
        print("Product Price: ", self.price)

