"""
    File: whats-my-acronym.py
    Author: FernandMX20
    Created On: Tue Jun 08 2021
    e-mail: fernandoaguilarserment@gmail.com
    Description:
        This is a series of projects or exercises on python, proposed on FreeCodeCamp
        https://www.freecodecamp.org/news/python-projects-junior-developers/
"""

print("Enter the full meaning of a organization or concept")
print("for example, United Nations")

org = input("Enter the name: ") # ask the user to enter the info requested

devide = org.split()    # now split ths string ...

# ... and for heach word, extract the first letter ...
for i in devide:
    print(i[0].capitalize(),end="") # ... and print it on screen