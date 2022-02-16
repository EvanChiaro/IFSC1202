N = int(input("Enter Number: "))
x = 1
y = 0
for i in range(1,N+1) :
    x *= i
    y += x
print(y)