s = input("Enter a string: ")
first = s.find('h')
second = s.rfind('h') + 1
a = s[first:second]
print(s[:first] + a[::-1] + s[second:])