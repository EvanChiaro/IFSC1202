N = int(input("Enter N: "))
for i in range(1,N+1) :
    x = 0
    for j in range(i) :
        x += 1
        print(str(x), end='')