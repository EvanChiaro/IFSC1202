a = []
sales = open("CarSales.txt")
x = sales.readline()
while x != '':
    y = x.split(',')
    a.append(y)
    x = sales.readline()
cars = 0
avg = 0
for i in range(len(a)):
    cars += 1
    avg += int(a[i][1])
avg = round(avg / cars)
print("{} Total Cars - Average Price: ${}".format(cars, avg))
def make_search(a, n):
    total = 0
    price = 0
    for i in range(len(a)):
        if a[i][0] == n:
            total += 1
            price += int(a[i][1])
    if total == 0:
        print("Car Make Not Found")
    else:
        price = round(price / total)
        dif = round(((price-avg)/price * 100), 2)
        print("    {} Cars Found".format(total), "${} Avergae Price".format(price), "{:.2f}% Above/Below Average".format(dif), sep='\n')
def proper_case(n):
    if len(n) == 3:
        n = n.upper()
    else:
        n = n.title()
    return n
n = input("Enter Car Make: ")
while n != '':
    n = proper_case(n)
    make_search(a, n)
    n = input("Enter Car Make: ")