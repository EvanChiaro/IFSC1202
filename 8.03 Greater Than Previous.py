x = input("Enter values separated by spaces: ")
y = x.split()
z = 0
for i in range(len(y)):
    y[i] = int(y[i])
    if y[i]>z and i>0:
        print(y[i])
    z = y[i]