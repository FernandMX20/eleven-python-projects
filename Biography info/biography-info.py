"""
    File: biography-info.py
    Author: FernandMX20
    Created On: Thu Jun 03 2021
    e-mail: fernandoaguilarserment@gmail.com
    Description:
        This is a series of projects or exercises on python, proposed on FreeCodeCamp
        https://www.freecodecamp.org/news/python-projects-junior-developers/
"""

# this function checks if the information entered by the user is correct
def correct(sentence):
    for word in sentence:
        if(word != "*"):    # if the word not contains a *, return boolean True
            return True
        else:
            print("Enter a valid sentence again")   # else ask the user again for the info, return boolean False
            return False

# functions asking the user for the required biography info
def enterName():
    name = input("What's your name? ")
    return name

def enterBirthDate():
    birthDate = input("What's your date of birth? ")
    return birthDate

def enterAddress():
    address = input("What's your address? ")
    return address

def enterGoals():
    goals = input("What's your goals? ")
    return goals

""" within the while loop, check user's info and if it is wrong, ask again 
    if the sentence is correct, go on and finish loop """
print("Well mate, tell me something about you")
while(True):
    name = enterName()  # user's name
    if(correct(name)): 
        break

while(True):
    birthDate = enterBirthDate()  # user's birth date
    if(correct(birthDate)):
        break

while(True):
    address = enterAddress()  # user's address
    if(correct(address)):
        break

while(True):
    goals = enterGoals()  # user's personal goals
    if(correct(goals)):
        break
print("\n")

# finally, print on screen the info entered
print("Name: " + name)
print("Date of birth: " + birthDate)
print("Address: " + address)
print("Personal goals: " + goals)