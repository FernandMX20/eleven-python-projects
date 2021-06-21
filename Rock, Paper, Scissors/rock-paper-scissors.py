"""
    File: rock-paper-scissors.py
    Author: FernandMX20
    Created On: Mon Jun 14 2021
    e-mail: fernandoaguilarserment@gmail.com
    Description:
        This is a series of projects or exercises on python, proposed on FreeCodeCamp
        https://www.freecodecamp.org/news/python-projects-junior-developers/

        Following the tutorial:
        Python Programming - Creating a Rock, Paper, Scissors Game, by Tutorial Spot
        https://www.youtube.com/watch?v=5wfxO_juzYM
"""

from random import randint   # used for the random method for the randint function

pc_option = ["rock", "paper", "scissors"]   # so, rock = 0, paper = 1 and scissors = 2

print("Rock, paper, scissors game\n")
loop = True # to enter to the while loop
answer = input("Ready to play? - y/n: ")

while(answer == "y" and loop == True):    # if the variable is true, run into the loop
    pc_choice = pc_option[randint(0,2)]     # now the pc chooses the option
    user_choice = input("You choose: ")     # ask the user which option he chooses
    print("the pc choose: " + pc_choice)    # and show the pc choice

    if user_choice == pc_choice:
        print("It's a draw")
    elif user_choice == "rock" and pc_choice == "paper":
        print("PC wins")
    elif user_choice == "rock" and pc_choice == "scissors":
        print("User wins")
    elif user_choice == "paper" and pc_choice == "rock":
        print("User wins")
    elif user_choice == "paper" and pc_choice == "scissors":
        print("PC wins")
    elif user_choice == "scissors" and pc_choice == "rock":
        print("PC wins")
    elif user_choice == "scissors" and pc_choice == "paper":
        print("User wins")

    answer = input("want to try again? - y/n: ")    # once finished, it asks the user whether or not to repeat the game 