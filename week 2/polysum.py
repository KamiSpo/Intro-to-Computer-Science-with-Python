import math
def polysum(n, s):

    if n >= 3:

        area = (0.25 * n * s**2) / math.tan(math.pi/n)
        perimeter_sq = (n * s)**2

        out = round((area + perimeter_sq), 4)

        return out
    
    else: 
        print("n has to be greater than 3")


