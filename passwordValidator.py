userInput = input("Enter a password to validate: ")

is7Characters = False
has2Integers = False
has2SpecialChars = False

specialCharacters = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
integerValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

userList = list(userInput)

if len(userList) >= 7:
    is7Characters = True


spCount = 0
for i in userList:
    for j in specialCharacters:
        if i == j:
            spCount += 1

intCount = 0
for i in userList:
    for j in integerValues:
        if i == j:
            intCount += 1

if (spCount >= 2 and intCount >=2):
    has2Integers = True
    has2SpecialChars = True

if (is7Characters == True and has2Integers == True and has2SpecialChars == True):
    print('Strong')
else:
    print('Weak')