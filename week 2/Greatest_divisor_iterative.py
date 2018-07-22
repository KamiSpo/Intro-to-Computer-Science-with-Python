def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a >= b:
        test = b
    else:
        test = a

    for test in range(test, 0, -1):
        if a % test == 0 and b % test == 0:
            return test

