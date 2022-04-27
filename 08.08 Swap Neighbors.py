x = input("Enter values separated by spaces: ")
y = x.split()
c = []
for i in range(len(y)):
    if i%2==1:
        a = y[i-1]
        b = y[i]
        c += b + a
    elif i==len(y)-1:
        c += y[i]
print(' '.join(c))