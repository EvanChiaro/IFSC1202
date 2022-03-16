x = input("Enter values separated by spaces: ")
y = x.split()
z = 0
for i in range(len(y)):
    y[i]=int(y[i])
    if y[i]<0 and z<0 and i!=0:
        print(z, y[i])
    elif y[i]>=0 and z>=0 and i!=0:
        print(z, y[i])
    z = y[i]