
from collections import defaultdict


# Challenge 371 (easy)
# Takes in single numerical input and figures out additive persistence, ie add digits together until you get to a single digit.
# https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/
def Challenge371E():
    number = input("Provide a number for additive persistence... ")
    steps = 0
    while len(number) > 1:
        numberArray = list(number)
        newNumber = 0
        for i in numberArray:
            newNumber += int(i)

        number = newNumber
        steps += 1

    return steps

# Challenge 372 (easy)
# Takes in a lower case string of x and y and determines the count is equal or not.
# https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/
def Challenge372E():
    string = input("Provide an input of characters... ")

    xCount = string.count("x")
    yCount = string.count("y")
    return xCount == yCount

# Challenge 372 (easy) Bonus
# Takes in a lower case string and works out if all lowercase characters occur the same number of times.
# https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/
def Challenge372E_Bonus():
    string = input("Provide a string of lowercase Characters...")
    dictionary = {}
    dictionary = defaultdict(int)

    for char in string:
        if char.islower():
            dictionary[char] += 1

    charCount = None
    for key, value in dictionary.items():
        if charCount == None:
            charCount = value
        elif charCount != value:
            return False        

    return True

print(Challenge372E_Bonus())