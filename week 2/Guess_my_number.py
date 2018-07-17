low = 0
high = 100
guess =(low + high)/2
x = "e"


print("Please think of a number between 0 and 100!")

while x is not "c":
    print("Is your secret number " + str(int(guess)) + "?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if x is "h":
        high = guess
    elif x is "l": 
        low = guess
    elif x is "c":
        print("Game over. Your secret number was: " + str(int(guess)))
    else: 
        print("Sorry, I did not understand your input.")
    guess =(low + high)//2



