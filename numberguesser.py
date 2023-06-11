import random
min = int(input("What is the minimum number?"))
max = int(input("What is the maximum number?"))
ran = int(random.randrange(min + 1, max + 1))
attempts = 3;
while attempts > 0:
    userGuess=int(input("What is your guess?"))
    if userGuess == ran:
        print("Congratulations! You guessed the number!")
        break
    elif userGuess < ran:
        print("Your guess is too low!")
        attempts -= 1
    if userGuess > ran:
        print("Your guess is too high!")
        attempts -= 1