def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    tmp = []
    for letter in secretWord:
        if letter in lettersGuessed:
            tmp.append(letter)
        else: 
            tmp.append(" _ ")
    
    currentGuess = ''.join(tmp)
    return currentGuess

