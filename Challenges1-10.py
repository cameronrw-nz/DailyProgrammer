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
       
Challenge1H()