# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "p0300_words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
    # https://docs.python.org/zh-cn/3/library/functions.html?highlight=all#all
    return all([i in lettersGuessed for i in secretWord])

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordGuessed = ['_'] * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            wordGuessed[i] = secretWord[i]
    return ''.join(wordGuessed)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    for char in lettersGuessed:
        if char in alphabet:
            alphabet.remove(char)
    return ''.join(alphabet)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    lettersGuessed = []
    
    true = "Good guess:"
    false = "Oops! That letter is not in my word:"
    already = "Oops! You've already guessed that letter:"
    reply = {"t": true, "f": false, "already": already}
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    
    while True:
        print("-----------")
        print("You have {} guesses left.".format(guesses))
        print("Available letters:", getAvailableLetters(lettersGuessed))
        
        letterGuessed = input("Please guess a letter: ").lower()
        
        if letterGuessed in secretWord and letterGuessed not in lettersGuessed:
            state = "t"
            lettersGuessed.append(letterGuessed)
        elif letterGuessed not in secretWord and letterGuessed not in lettersGuessed:
            state = "f"
            guesses -= 1
            lettersGuessed.append(letterGuessed)
        elif letterGuessed in lettersGuessed:
            state = "already"
        
        print(reply[state], getGuessedWord(secretWord, lettersGuessed))
        
        if guesses == 0:
            print("-"*11 + "\nSorry, you ran out of guess. The word was else.")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print("-"*11 + "\nCongratulations, you won!")
            break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print("debug -- secret word is:", secretWord)
hangman(secretWord)