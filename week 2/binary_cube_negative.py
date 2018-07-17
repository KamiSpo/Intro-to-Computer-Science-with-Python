x = -27
low = x
high = 0
guess = (high + low)/2
print(guess)
epsilon = 0.01

while abs(x - guess**3) >= epsilon:
    if guess**3 <= x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2

if abs(x - guess**3 >= epsilon):
    print("X is not perfect cube")
else:
    print("Cube of " + str(x) + " is: " + str(guess))



