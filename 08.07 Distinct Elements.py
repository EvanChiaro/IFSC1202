x = input("Enter values in ascending order, separated by spaces: ")
y = x.split()
z=1
for i in range(len(y)):
    if y[i]>y[i-1]:
        z+=1
print("Number of distinct elements: " + str(z))