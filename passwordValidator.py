from string import digits as ints
from string import punctuation as spChars
#Takes user input that will be the password to be validated
userInput = input("Enter a password to validate: ")

#Flags set for all conditions to be checked as flase
is7Characters = False
has2Integers = False
has2SpecialChars = False

#Converting user input string to list for each character manipulation
userList = list(userInput)

#Condition check if the length of password is or greater than 7
if len(userList) >= 7:
    is7Characters = True

#Condition check if the number of special characters is more than 2
if len(set(spChars) & set(userList)) >= 2:
    has2SpecialChars = True

#Condition check if the number of integers is more than 2
if len(set(ints) & set(userList)) >= 2:
    has2Integers = True

#Condition check for all the flags to be true if yes, then print out strong else print out weak
if (is7Characters == True and has2Integers == True and has2SpecialChars == True):
    print('Strong')
else:
    print('Weak')