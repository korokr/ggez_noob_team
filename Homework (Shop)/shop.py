import product as p

class Shop:
    def __init__(self, products = [], shop_name = "Name of shop default"):
        self.products = products
        self.shop_name = shop_name
        self.alcohol = []
        self.meat = []
        self.sweets = []

    def addAlcohol(self, product = p.Product()):
        self.alcohol.append(product.name)

    def addMeat(self, product = p.Product()):
        self.meat.append(product.name)

    def addSweets(self, product = p.Product()):
        self.sweets.append(product.name)


    def showShop_name(self):
        if(self.shop_name != None or self.shop_name != ""):
            print(f"Shop name {self.brand}")
        else:
            print("The attribute name is empty or none!")