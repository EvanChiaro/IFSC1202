class RetailItem ():
    def __init__(self, Desc="", UnitsOnHand=0, Price=0):
        self.Desc=Desc
        self.UnitsOnHand=UnitsOnHand
        self.Price=Price
    def InventoryValue(self):
        value = self.UnitsOnHand * self.Price
        return value
def print_inventory(list):
    print("{:>11s}{:>20s}{:>20s}{:>20s}".format("Description", "Units On Hand", "Price", "Inventory Value"))
    for i in range(len(list)):
        print("{:>11s}{:>20.2}{:>20s}{:>20.2f}".format(list[i].Desc, str(list[i].UnitsOnHand), str(list[i].Price), list[i].InventoryValue()))
    print()
def inventory_search(list, listitem):
    for i in range(len(list)):
        if list[i].Desc == listitem:
            return i
    return -1
itemlist = []
itemfile = open("11.01 Inventory.txt")
x = itemfile.readline()
while x != "":
	y = x.split(",")
	item = RetailItem(y[0].strip(), float(y[1].strip()), float(y[2].strip()))
	itemlist.append(item)
	x = itemfile.readline()
itemfile.close()
print_inventory(itemlist)
update = []
updatefile = open("11.01 Inventory.txt")
x = updatefile.readline()
while x != "":
	y = x.split(",")
	itemlist[inventory_search(itemlist, y[0])].Price = float(y[2])
	x = updatefile.readline()
updatefile.close()
print_inventory(itemlist)
