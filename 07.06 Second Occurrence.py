s = input("Enter a string: ")
a = s.count('f')
if a > 1:
    print(s.find('f', s.find('f') + 1))
elif a == 1:
    print("One f")
else:
    print("Zero f")