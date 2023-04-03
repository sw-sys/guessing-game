# Improved from "coding for beginners" - McGrath exercises

import random

num = random.randint(1 , 100)
flag = True
guess = 0

while flag:
    guess = input("Guess the number I've choosen from 1 to 100: ")

    if not guess.isdigit():
        try:
            int(guess)
        except ValueError:
            print("Invalid entry - enter a number 1 to 100")
            break

    elif int(guess) < num:
        print("Guess is too low")

    elif int(guess) > num:
        print("Guess is too high")

    else:
        print(f"That's correct! My number was", num)
        Flag = False