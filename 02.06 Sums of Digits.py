x = input("Enter a three digit number: ")
y = int(x) / 100
z = int(x) % 100 / 10
a = int(x) % 10
sum = int(y) + int(z) + int(a)
print("Sum of Digits: {}".format(sum))