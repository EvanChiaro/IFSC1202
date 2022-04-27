n = input("Enter Size: ")
n = int(n)
a = []
b = []
b.append('+')
for i in range(n):
    b.append('-')
b.append('+')
a.append(b)
for i in range(n):
    b = []
    b.append('|')
    for j in range(n):
        b.append(' ')
    b.append('|')
    a.append(b)
b = []
b.append('+')
for i in range(n):
    b.append('-')
b.append('+')
a.append(b)
for i in range(len(a)):
    for j in range(len(a[i])):
        if i % 2 == 1 and j % 2 == 0 and a[i][j] == ' ':
            a[i][j] = '*'
        elif i % 2 == 0 and j % 2 == 1 and a[i][j] == ' ':
            a[i][j] = '*'
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='')
    print()