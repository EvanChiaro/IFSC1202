class RetailItem:
    def __init__(self, desc="", untis=0, price=0):
        self.Description = desc
        self.UnitsOnHand = untis
        self.Price = price
    def InventoryValue(self):
        value = self.UnitsOnHand * self.Price
        return value
items = open("10.02 Inventory.txt")
item = items.readline()
item = item.split(',')
item1 = RetailItem(item[0], float(item[1]), float(item[2]))
item = items.readline()
item = item.split(',')
item2 = RetailItem(item[0], float(item[1]), float(item[2]))
item = items.readline()
item = item.split(',')
item3 = RetailItem(item[0], float(item[1]), float(item[2]))
print("Description".rjust(11), "Units On Hand".rjust(15), "Price".rjust(7), "Inventory Value".rjust(17))
print(str(item1.Description).rjust(11), str(item1.UnitsOnHand).rjust(15), str(item1.Price).rjust(7), "{0:.2f}".format(item1.InventoryValue()).rjust(17))
print(str(item2.Description).rjust(11), str(item2.UnitsOnHand).rjust(15), str(item2.Price).rjust(7), "{0:.2f}".format(item2.InventoryValue()).rjust(17))
print(str(item3.Description).rjust(11), str(item3.UnitsOnHand).rjust(15), str(item3.Price).rjust(7), "{0:.2f}".format(item3.InventoryValue()).rjust(17))