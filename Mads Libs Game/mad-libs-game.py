"""
    Archivo: mad-libs-game.py
    Autor: FernandMX20
    Fecha: Tue May 18 2021
    e-mail: fernandoaguilarserment@gmail.com
    Description:
        This is a series of projects or exercises on python, proposed on FreeCodeCamp
        https://www.freecodecamp.org/news/python-projects-junior-developers/
"""
loop = True     # True loop to enter in the while cicle

print("Mad libs game")

while(loop == True):    # while the loop is true, run the while cicle
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    name = input("Enter a name: ")

    # print the final result
    print("The other day, " + name + " and I saw a " + noun + ", it was " + adjective + ". Then we " + verb + " for a while.")

    print("Repeat the game?: ")     # ask the user to replay the game
    repeat = input("Y/N: ")
    if(repeat == "Y" or repeat == "y"):
        print("Here we go again!")  # to be true
        loop = True
    elif(repeat == "N" or repeat == "n"):
        print("Bye, see you soon!")  # otherwise the program ends
        loop = False
        break
