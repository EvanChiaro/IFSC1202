radius = open("06.01 Radius.txt")
from math import pi
width = 15
def diameter(r):
    dia = float(r) * 2
    return dia
def circumference(r):
    cir = float(r) * pi * 2
    return cir
def area(r):
    area = pi * float(r)**2
    return area
heading = str("Radius".rjust(width) + "Diameter".rjust(width) + "Circumference".rjust(width) + "Area".rjust(width))
print(heading)
r = radius.readline()
while r != "":
    print(str(float(r)).rjust(width) + str(round(diameter(r),5)).rjust(width) + str(round(circumference(r), 5)).rjust(width) + str(round(area(r), 5)).rjust(width), sep="")
    r = radius.readline()
radius.close()