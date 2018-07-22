def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    out = 1
    if exp == 0:
        return 1
    else:
        for exp in range(1, exp + 1):
            out = out * base
        return out
        