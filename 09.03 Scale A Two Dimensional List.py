def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
def scale_list(a, s):
    for i in range(len(a)):
        for j in range(len(a[i])):
            t = a[i][j]
            t = t*2
            a[i][j] = t
a = []
data = open("09.03 NumbersList.txt")
x = data.readline()
while x != "":
    y = x.split()
    for i in range(len(y)):
        y[i] = int(y[i])
    a.append(y)
    x = data.readline()
print_list(a)
x = input("Enter scale value: ")
scale_list(a, x)
print_list(a)