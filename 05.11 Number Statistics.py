i = 1
sum, max, count, min = 0 , 0, 0, 0
while i == 1:
    x = float(input("Enter a Value (zero to quit): "))
    sum += x
    if x == 0:
        i = 2
    else:
        count += 1
    if x > max:
        max = x
    if min == 0:
        min = x
    elif min > x and x != 0:
        min = x
average = sum / count
print("Count: {}".format(count), "Sum: {}".format(sum), "Average: {}".format(average), "Minimum: {}".format(min), "Maximum: {}".format(max), sep='\n')
