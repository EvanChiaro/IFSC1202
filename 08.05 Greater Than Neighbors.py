x = input("Enter values separated by spaces: ")
y = x.split()
for i in range(len(y)):
    a = y[i-1]
    b = y[i]
    c = y[i+1]
    if b>a and b>c:
        print(b)