x = 27
high = x
low = 0
guess = (high + low)/2
epsilon = 0.01

while abs(x - guess**3) >= epsilon:
    print(guess)
    if guess**3 >= x:
        high = guess
    else:
        low = guess
    guess = (high + low)/2

if abs(x - guess**3 >= epsilon):
    print("X is not perfect cube")
else:
    print("Cube of " + str(x) + " is: " + str(guess))



