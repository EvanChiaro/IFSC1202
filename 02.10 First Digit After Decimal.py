x = input("Enter Number: ")
y = float(x) - int(float(x)) - 0.05
z = round(y,1)
a = z * 10
print("Tenths Value: {}".format(int(a)))