x = input("Enter values separated by spaces: ")
y = x.split()
z = []
for i in range(len(y)):
    a = y[i]
    for j in range(len(y)):
        b = y[j]
        if a == b and i != j:
            check = 0
            break
        else:
            check = 1
    if check ==1:
        z += a
print("Unique Elements: " + ' '.join(z))