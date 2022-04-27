x = input("Enter values separated by spaces: ")
y = x.split()
a = min(y)
b = max(y)
c = y.index(a)
d = y.index(b)
z = []
for i in range(len(y)):
    if i == c:
        z += y[int(d)]
    elif i == d:
        z += y[int(c)]
    else:
        z += y[i]
print(' '.join(z))