pops = open("08.11 USPopulation.txt")
x = pops.readline()
z = []
listchange = []
while x != '':
    z.append(x)
    x = pops.readline()
print("Year".ljust(7) + "Population".ljust(13) + "Change".ljust(10) + "Percent Change".ljust(15))
for i in range(len(z)):
    year = 1950 + i
    pop = int(z[i]) * 1000
    if i != 0:
        change = (int(z[i]) - int(z[i-1])) * 1000
        listchange.append(change)
    else:
        change = 'N/A'
    if i != 0:
        pchange = round(change / (int(z[i-1])*1000), 2)
    else:
        pchange = 'N/A'
    print(str(year).ljust(7) + str(pop).ljust(13) + str(change).ljust(10) + (str(pchange) + '%').ljust(10))
print()
total = 0
for i in range(len(listchange)):
    y = listchange[i]
    total += int(y)
avg = total / 40
minyear = int(listchange.index(min(listchange))) + 1951
maxyear = int(listchange.index(max(listchange))) + 1951
print("Average Change = " + str(avg), "Minimum Change = " + str(min(listchange)) + " ({})".format(minyear), "Maximum Change = " + str(max(listchange)) + " ({})".format(maxyear), sep='\n')