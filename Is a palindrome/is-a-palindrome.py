"""
    File: is-a-palindrome.py
    Author: FernandMX20
    Created On: Mon Jun 21 2021
    e-mail: fernandoaguilarserment@gmail.com
    Description:
        This is a series of projects or exercises on python, proposed on FreeCodeCamp
        https://www.freecodecamp.org/news/python-projects-junior-developers/
"""

def isPalindrome(word):     # use a function to check for palindrome 
    if(word == word[::-1]): # compare the original word to his inverse
        print(word + " is palindrome")
    else:
        print(word + " is not palindrome")

count = 5
while(count >= 1):  # ask the user for five words
    word = input("Give me a word to check if it is a palindrome: ")
    isPalindrome(word)  # and call the function
    count -=1   # 

