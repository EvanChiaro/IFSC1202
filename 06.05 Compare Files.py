filea = open("06.05 CompareFileA.txt")
fileb = open("06.05 CompareFileB.txt")
line = 0
dif = 0
a = filea.readline()
b = fileb.readline()
while a != "" and b != "":
    line += 1
    if a != b:
        print("Line: " + str(line) + " - Flie A: " + a)
        print("Line: " + str(line) + " - Flie B: " + b)
        dif += 1
    a = filea.readline()
    b = fileb.readline()
print(str(dif) + " differences")