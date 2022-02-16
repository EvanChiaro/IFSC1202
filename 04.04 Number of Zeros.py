N = int(input("Enter Number: "))
y = 0
for i in range(N) :
    x = int(input("Enter Number: "))
    if x == 0 :
        y += 1
print("Number of Zeros: " + str(y))