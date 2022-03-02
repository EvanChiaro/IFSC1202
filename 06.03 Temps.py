def FahrToCel(tf):
    tc = round((tf - 32) * 5/9, 1)
    return tc
tempf = open("06.03 FTemps.txt")
tempc = open("06.03 CTemps.txt", "a")
records = 0
tf = tempf.readline()
while tf != "":
    tempc.write(str(FahrToCel(float(tf))).ljust(5) + "\n")
    records += 1
    tf = tempf.readline()
print(str(records) + "records written")
