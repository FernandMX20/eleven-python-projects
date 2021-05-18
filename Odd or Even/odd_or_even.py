"""
    Archivo: odd_or_even.py
    Autor: FernandMX20
    Fecha: Tue May 04 2021
    e-mail: fernandoaguilarserment@gmail.com
    Description:
        This is a series of projects or exercises on python, proposed on FreeCodeCamp
        https://www.freecodecamp.org/news/python-projects-junior-developers/
"""
print("Hello there, add a number between 1 and 1000")   # Welcomes the user and request for a number
number = int(input("What number are you thinking?: "))  # the number will be converted to an integer before moving to the logical condition

if number >= 1 and number <= 1000:  # In the if statement, if the number is greater than one and less than a thousand
    if number % 2 == 0:     # now if the number is odd ...
        print("That's an odd number! Have another?")    # ... print the odd line
    else:
        print("That's an even number! Have another?")   # else the even line