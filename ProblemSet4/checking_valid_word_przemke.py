# TODO: delete this:
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    # Check if this word even exists.
    if word not in wordList:
        return False

    # Dict similar as `hand` but calculated for word we are checking against
    word_dict = {}
    for l in word:
        if l not in word_dict:
            word_dict[l] = 0
        word_dict[l] += 1

    # Check how many letters our word is using and compare it to number of 
    # available letters
    for letter, wrd_letter_count in word_dict.items():
        if hand.get(letter, 0) < wrd_letter_count:
            return False

    return True