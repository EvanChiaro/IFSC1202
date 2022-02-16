from random import randint
name = input("Hello! What is your name? ")
print("Well, {}, I am thinking of a number between 1 and 20.".format(name), "You have 5 guesses.", sep="\n")
x = randint (1,20)
i = 1
while i<6 :
    y = int(input("Take a guess: "))
    if y < x :
        print("Your guess is too low.")
    elif y > x :
        print("Your guess is too high.")
    else:
        print("Good job, {}, you guessed my number in {} guesses!".format(name, str(i)))
        i = 7
    i += 1
if i == 6 :
    print("Nope. The number I was thinking of was {}.".format(x))