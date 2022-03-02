numbers = open("06.06 Numbers.txt")
def isEven(n):
    x = int(n) % 2
    if x == 1:
        return False
    else:
        return True
def isOdd(n):
    y = int(n) % 2
    if y == 1:
        return True
    else:
        return False
def isPrime(n):
    for z in range(2, int(n)):
        a = int(n) % z
        if a == 0:
            break
    if a == 0:
        return False
    else:
        return True
even = open("06.06 Evennumbers.txt", "a")
odd = open("06.06 Oddnumbers.txt", "a")
prime = open("06.06 Primenumbers.txt", "a")
evencount = 0
oddcount = 0
primecount = 0
read = 0
n = numbers.readline()
while n != "":
    read += 1
    if isEven(n) == True:
        even.write(n)
        evencount += 1
    if isOdd(n)  == True:
        odd.write(n)
        oddcount += 1
    if isPrime(n) == True:
        prime.write(n)
        primecount += 1
    n = numbers.readline()
print(str(evencount) + " even numbers", str(oddcount) + " odd numbers", str(primecount) + " prime numbers", str(read) + " numbers read", sep="\n")
even.close()
odd.close()
prime.close()
numbers.close()