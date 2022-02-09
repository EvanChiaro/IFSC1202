x = input("Enter two digit number: ")
y = int(x) % 10
print("Ones Digit: " + str(y))
print("Tens Digit: " + "{:^1.1}".format(x))