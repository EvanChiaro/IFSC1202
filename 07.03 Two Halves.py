s = input("Enter a string: ")
n = len(s)
first = round(n/2)
second = round(n-n/2)
print(s[second:] + s[:first])