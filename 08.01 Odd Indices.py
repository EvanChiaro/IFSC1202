x = input("Enter values separated by spaces: ")
y = x.split()
for i in range(len(y)):
   y[i] = int(y[i])
for i in range(len(y)):
    if i%2==0:
        print(y[i])