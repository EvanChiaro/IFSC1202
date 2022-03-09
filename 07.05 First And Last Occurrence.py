s = input("Enter a string: ")
a = s.count('f')
if a == 1:
    print(s.find('f'))
elif a > 1:
    print(s.find('f'), s.rfind('f'))
else:
    print(0)