# Challenge 1 (easy)
# Takes in 3 user input and outputs a single string.
# https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
def Challenge1E():
    name = input("What's your name? ")
    age = input("What's your age? ")
    username = input("What's your username? ")

    print("Your name is " + name + ", you are " + age + " years old, and your Username is " + username)

# Challenge 1 (Hard)
# Pick a number between 1-100 and computer guesses your number based on user feedback
# https://www.reddit.com/r/dailyprogrammer/comments/pii6j/difficult_challenge_1/
def Challenge1H():
    floor = 0
    ceiling = 100
    input("Pick a number between 1-100")

    while ceiling > floor:
        guessedValue = (ceiling+floor)//2
        userInput = input("Is your number " + str(guessedValue) + "? ")
        if (userInput == "higher"):
            floor = guessedValue
        elif (userInput == "lower"):
            ceiling = guessedValue
        elif (userInput == "yes"):
            print("Your number is " + str(guessedValue))
            break
        if (floor == ceiling):
            print(str(floor) + " is your number")
            break
        if (floor+1 == ceiling):
            print(str(floor+1) + " is your number")
            break

# Challenge 2 (Easy)
# Implement a calculate that has impact on daily life (living in bangkok so converting money from Baht to NZD or visa-versa)
# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
def CurrencyConverter(amount, isConvertingToThb):
    # Can be improved by retrieving conversion rate from external sauce
    nzdToThb = 21.49
    if (isConvertingToThb == True):
        return float(amount) * nzdToThb
    else:
        return float(amount) / nzdToThb

def Challenge2E():
    currency = input("Pick currency to convert to, THB or NZD? ")
    amount = input("What is your amount in the original currency? ")

    convertedValue = 0
    if (currency.lower() == "thb"):
        convertedValue = CurrencyConverter(amount, True)
    else:
        convertedValue = CurrencyConverter(amount, False)
    
    print("Your amount (" + amount + ") in " + currency.upper() + " is " + str(convertedValue))
    
Challenge2E()