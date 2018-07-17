x = 0.8
high = 1
low = x
guess = (high + low)/2
print(guess)
epsilon = 0.00001

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
