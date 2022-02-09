a = input("Enter first two digit number: ")
b = input("Enter second two digit number: ")
one = int(a) / 10
three = int(a) % 10
two = int(b) / 10
four = int(b) % 10
print("Merged Number: {}{}{}{}".format(int(one), int(two), int(three), int(four)))