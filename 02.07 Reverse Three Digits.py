x = input("Enter a three digit number: ")
y = int(x) / 100
z = int(x) % 100 / 10
a = int(x) % 10
print("Reverse of digits: {}{}{}".format(int(a), int(z), int(y)))