import product as p
import shop as sh

jack_daniels = p.Product(1, "Jack Daniels")
pinot_noir = p.Product(1, "Pinot Noir")
sauvignon_blanc = p.Product(1, "Sauvignon Blanc")

sausage = p.Product(0, "Sausage")
chicken_wings = p.Product(0, "Chicken Wings")
smoked_sausage = p.Product(0, "Smoked Sausage")

cookies = p.Product(2, "Cookies")
muffins = p.Product(2, "Muffins")
candies = p.Product(2, "Candies")

products = [jack_daniels, pinot_noir,  sauvignon_blanc, sausage, chicken_wings, smoked_sausage, cookies, muffins, candies]
atb = sh.Shop(shop_name = "ATB")
for product in products:
    if(product.role == 1):
        atb.addAlcohol(product)
    if(product.role == 0):
        atb.addMeat(product)
    if(product.role == 2):
        atb.addSweets(product)
print(f"Alcohol = {atb.alcohol}")
print(f"Meat = {atb.meat}")
print(f"Sweets = {atb.sweets}")