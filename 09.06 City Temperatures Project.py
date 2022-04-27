temps = open("09.06 CityTemps.txt")
a = []
t = temps.readline()
while t != '':
    x = t.split()
    a.append(x)
    t = temps.readline()
temps.close
for i in range(len(a)):
    total = 0
    for j in range(len(a[i])):
        if j != 0:
            total += int(a[i][j])
    avg = int(total / (len(a[i]) - 1))
    a[i].append(avg)
print("City".ljust(9), "Mo".ljust(9), "Tu".ljust(9), "We".ljust(9), "Th".ljust(9), "Fr".ljust(9), "Sa".ljust(9), "Su".ljust(9), "Avg".ljust(9), sep='')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(str(a[i][j]).ljust(9), end='')
    print()