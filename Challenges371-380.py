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

print(Challenge371E())