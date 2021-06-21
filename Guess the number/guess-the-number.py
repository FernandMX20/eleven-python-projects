"""
    File: guess-the-number.py
    Author: FernandMX20
    Created On: Mon Jun 14 2021
    e-mail: fernandoaguilarserment@gmail.com
    Description:
        This is a series of projects or exercises on python, proposed on FreeCodeCamp
        https://www.freecodecamp.org/news/python-projects-junior-developers/
"""

import random   # used for the random method

loop = True # to enter to the while loop
answer = input("Ready to play? - y/n: ")
counter = 0 # start a counter for attempts

while(answer == "y" and loop == True):    # if the variable is true, run into the loop
    guessNumber = int(input("Guess a number between 1 and 50: "))
    if(guessNumber < 1 or guessNumber > 50):
        loop = True
        print("Ups! wrong number, choose a different number")  # if the answer is ok, repeat the loop 
    else:
        counter += 1    # and keep counting 
        if(guessNumber == random.randrange(1,50)):  # now, get a random number between 1 to 50
            print("Congratulation!!! You guessed the number " + str(guessNumber) + "in " + str(counter) + " attempts")
            answer = input("want to try again? - y/n: ")
        else:
            print("Nop, wrong number")
            answer = input("want to try again? - y/n: ")
