x = input("Enter values separated by spaces: ")
y = x.split()
z = max(y)
a = y. index(z)
print("Largest value: " + str(z), "Index of largest value: " + str(a), sep='\n')