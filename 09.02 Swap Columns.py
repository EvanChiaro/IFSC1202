def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[1])):
            print(a[i][j], end=' ')
        print()
def swap_columns(a, i, j):
    for k in range(len(a)):
        temp = a[k][i]
        a[k][i] = a [k][j]
        a[k][j] = temp
a = []
data = open("09.02 NumbersList.txt")
x = data.readline()
while x != "":
    y = x.split()
    for i in range(len(y)):
        y[i] = int(y[i])
    a.append(y)
    x = data.readline()
print_list(a)
swap = input("Enter the columns to swap: ")
z = swap.split()
for i in range(len(z)):
    z[i] = int(z[i])
swap_columns(a, z[0], z[1])
print_list(a)