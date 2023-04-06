class Product:
    def __init__(self, role = 0, name = "Product default falue"):
        self.name = name
        self.role = role
    def showName(self):
        if(self.name != None or self.name != ""):
            print(f"Name: {self.name}")
        else:
            print("The attribute name is empty or none!")