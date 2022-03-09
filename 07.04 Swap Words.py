s = input("Enter a string: ")
n = s.find(' ')+1
print(s[n:] + " " + s[:n])