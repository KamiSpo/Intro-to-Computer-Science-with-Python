def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableLetters = []

    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            availableLetters.append(letter)

    currentlyAvailable = ''.join(availableLetters)
    return currentlyAvailable

