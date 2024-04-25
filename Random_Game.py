import random
randNumber = random.randint(1, 100)

userGuess = None
Guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    Guesses+=1
    if(userGuess == randNumber):
        print("Congratulation! You guess right number.")
    else:
        if(userGuess > randNumber):
            print("Sorry! You guess wrong number, enter smaller number.")
        else:
            print("Sorry! You guess wrong number, enter larger number.")
     
print("You guess number in", Guesses, "times.")
