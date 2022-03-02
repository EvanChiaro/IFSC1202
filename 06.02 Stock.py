stock = open("06.02 Stock.txt")
width = 10
def percentchange(new):
    change = (new - old) / new * 100
    return change
print("Price".rjust(width) + " " + "Change".rjust(width))
old = 0
s = stock.readline()
while s != "":
    new = float(s)
    if old == 0:
        print(str(new).rjust(width))
    else:
        print(str(new).rjust(width) + " " + (str(round(percentchange(new),2)) + "%").rjust(width))
    old = float(s)
    s = stock.readline()