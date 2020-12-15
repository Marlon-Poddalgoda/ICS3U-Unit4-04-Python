#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program is an updated guessing game

import random
import constants


def main():
    # this function compares an integer to a random number
    #       with a loop

    print("Today we will play a guessing game.")

    # loop counter variable
    loop_counter = 0

    # random number generation
    random_number = random.randint(constants.MIN_GUESS,
                                   constants.MAX_GUESS)

    while True:
        # input
        print("")
        user_guess = input("Enter a number between 0-9: ")
        print("")

        # process
        try:
            user_guess_int = int(user_guess)

            if user_guess_int >= 0 and user_guess_int <= 9:

                loop_counter = loop_counter + 1

                if user_guess_int == random_number:
                    break
                elif user_guess_int > random_number:
                    # output
                    print("Your guess is too high, try again.")
                elif user_guess_int < random_number:
                    # output
                    print("Your guess is too low, try again.")
                else:
                    print("Error, please try again.")
            else:
                # output
                print("Your guess must be between {0}-{1}, try again."
                      .format(constants.MIN_GUESS, constants.MAX_GUESS))
        except Exception:
            # output
            print("That's not a number! Try again.")

    # correct output
    print("")
    print("Correct! It took you {} time(s) to guess the number"
          .format(loop_counter))
    # final output
    print("")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
