size = input("Enter the number of rows and columns: ")
x = size.split()
m = int(x[0])
n = int(x[1])
a = []
for i in range(m):
    y = input("Enter a line of data: ")
    z = y.split()
    a.append(z*1)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
z = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if z < int(a[i][j]) > int(a[i][j-1]):
            z = int(a[i][j])
            row = i + 1
            column = j + 1
print("The maximum value {} occurred in row {} column {}".format(z, row, column))