def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    indices = {}
    currentGuess = {}
    index = 0

    for letter in secretWord:
        #creating a dictionary from letters in secret word and their indices
        indices[index] = letter
        #preparing a new dictionary with same indices
        currentGuess[index] = []
        index += 1

    index = 0

    for letter in secretWord:
        if letter in lettersGuessed:
            #filling the new dictionary with guessed letters
            currentGuess[index] = letter
        else: 
            #filling empty fields with "_"
            currentGuess[index] = " _ "
        index += 1
        
    #converting a list to string
    currentGuessString = ''.join(currentGuess.values())
    return currentGuessString
    

           
getGuessedWord('wroclawek', ['f', 'i', 'a', 'l'])   
           
