#Takes user input that will be the password to be validated
userInput = input("Enter a password to validate: ")

#Flags set for all conditions to be checked as flase
is7Characters = False
has2Integers = False
has2SpecialChars = False

#Initializing List of Special Characters and Integers
specialCharacters = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
integerValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Converting user input string to list for each character manipulation
userList = list(userInput)

#Condition check if the length of password is or greater than 7
if len(userList) >= 7:
    is7Characters = True

#Condition check if the number of special characters is more than 2
spCount = 0
for i in userList:
    for j in specialCharacters:
        if i == j:
            spCount += 1

#Condition check if the number of integers is more than 2
intCount = 0
for i in userList:
    for j in integerValues:
        if i == j:
            intCount += 1

#Setting flags to true if intergers are 2 and special characters are 2 in the passsword
if (spCount >= 2 and intCount >=2):
    has2Integers = True
    has2SpecialChars = True

#Condition check for all the flags to be true if yes, then print out strong else print out weak
if (is7Characters == True and has2Integers == True and has2SpecialChars == True):
    print('Strong')
else:
    print('Weak')