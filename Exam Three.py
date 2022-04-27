class House():
    def __init__(self, address, sqft, price):
        self.Address = address
        self.Sqft = sqft
        self.Price = price
    def costpersqft(self):
        sqftcost = self.Price/self.Sqft
        return sqftcost
    def payment(self, ar, ny):
        n = ny * 12
        r = ar / 100 / 12
        num = r * ((1+r)**n)
        den = ((1+r)**n) - 1
        payment = self.Price * (num / den)
        return payment
houselist = []
housefile = open("Exam Three Houses.txt")
house = housefile.readline()
while house != '':
    h = house.split(", ")
    myhouse = House(h[0], int(h[1]), int(h[2]))
    houselist.append(myhouse)
    house = housefile.readline()
ar = int(input("Enter Interest Rate: "))
ny = int(input("Enter Years for Mortgage: "))
print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("Address", "Sq Ft", "SqFt Cost", "Price", "Payment"))
for i in range(len(houselist)):
    print("{:>14s}{:>14s}{:>14.2f}{:>14.2f}{:>14.2f}".format(str(houselist[i].Address), str(houselist[i].Sqft), houselist[i].costpersqft(), houselist[i].Price, houselist[i].payment(ar, ny)))