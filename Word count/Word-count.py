"""
    File: Word-count.py
    Author: FernandMX20
    Created On: Tue May 25 2021
    e-mail: fernandoaguilarserment@gmail.com
    Description:
        This is a series of projects or exercises on python, proposed on FreeCodeCamp
        https://www.freecodecamp.org/news/python-projects-junior-developers/
"""

# Ask the user for a longer thought
thought = input("what's on your mind today?: ")

counter=0   #Initiate the counter of words

#   Separate each word between espaces
for word in thought.split():
    counter +=1     # and keep the count

print("oh, nice, you just told me what's on your mind in " + str(counter) + " words!")
