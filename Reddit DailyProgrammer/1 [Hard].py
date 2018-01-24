# Exercise 1 - Hard
# We all know the classic "guessing game" with higher or lower prompts.
# Lets do a role reversal; you create a program that will guess numbers between 1-100
# and respond appropriately based on whether users say that the number is too high or too low.
# Try to make a program that can guess your number based on user input and great code!
#
# Personal message : I will do two game modes for this exercise

import random


def mode1():
    num_to_find = random.randint(0, 100)
    print("Okay let's go ! Between 0 and 100. Guess :)")
    while True:
        try:
            guessed_num = int(input())

            if guessed_num > num_to_find:
                print("Too high ! Guess lower :)")
            elif guessed_num < num_to_find:
                print("Too low ! Guess higher :)")
            elif guessed_num == num_to_find:
                print(":o ! You found it ! :D Well played mate, it was {} !\nYou wanna play again ?"
                      " Okay, just pick a game mode, then :)".format(num_to_find))
                break
            else:
                print("\nDude. Between 0 and 100. Come on, guess ! :)")

        except ValueError:
            print("\nPlease fella, give me a number between 0 and 100, nothing else. Guess ! :)")
    select_mode()


def mode2():
    print("You wanna play against me ? Okay let's play, then.")

    lowest_number_possible = 0
    highest_number_possible = 100
    choice = 0

    while True:
        rand_num = random.randint(lowest_number_possible, highest_number_possible)

        print("Is it ... {} ?\n"
              "1 - Higher\n2 - Lower\n3 - That's the number !".format(rand_num))

        while True:
            try:
                choice = int(input())

                if choice == 1:
                    print("Higher, okay..")
                    lowest_number_possible = rand_num
                    break

                elif choice == 2:
                    print("Lower, okay..")
                    highest_number_possible = rand_num
                    break

                elif choice == 3:
                    print("Ooooh baby ! I won ! I found it ! It was {} !".format(rand_num))
                    break
                else:
                    print("\nPlease fella, either 1 - Higher or 2 - Lower. Nothing else.")

            except ValueError:
                print("\nPlease fella, either 1 - Higher or 2 - Lower. Nothing else.")

        if lowest_number_possible == highest_number_possible:
            print("Wait.. I.. I got it, right ? That's {} ?? YEAH !".format(lowest_number_possible))
            break

        if choice == 3:
            break
    print("\nYou wanna play again ? Okay, just pick a game mode, then :)")
    select_mode()


def select_mode():
    while True:
        game_mode = input()
        try:
            if int(game_mode) == 1:
                mode1()
                break
            elif int(game_mode) == 2:
                mode2()
                break
            elif int(game_mode) == 3:
                print("Okay see ya ! :D")
                exit()
            else:
                print("\nPlease fella, either 1- you want to find my number, or 2- you want me to find your number."
                      ". Or 3 - You want to leave, maybe ? Choose wisely !")

        except ValueError:
            print("\nPlease fella, either 1- you want to find my number, or 2- you want me to find your number."
                  ". Or 3 - You want to leave, maybe ? Choose wisely !")


print("Welcome here, fella !\n\n"
      "1 - Do you want to find my number ?\n"
      "2 - Do you want me to find your number ?\n"
      "3 - Do you want to leave ?")
select_mode()
