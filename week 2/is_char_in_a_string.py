def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False

    test_idx = len(aStr)//2
    test = aStr[test_idx]

    if len(aStr) == 1:
        return test == char
    else: 
        if char > test:
            return isIn(char, aStr[test_idx + 1:len(aStr)])
        elif char < test: 
            return isIn(char, aStr[:test_idx])
        else:
            return True
