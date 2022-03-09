s = input("Enter a string: ")
first = s.find('h')
second = s.rfind('h') + 1
print(s[:first] + s[second:])