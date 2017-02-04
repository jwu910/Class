# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

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
secretWord = chooseWord(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += 1
    if guessed == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord_list = []
    secretWord_guess = []
    for wordLen in range(0,len(secretWord)):
        secretWord_guess.append('_ ')
    secretWord_list = list(secretWord)
    letIndex = 0
    while letIndex < len(secretWord):
        if secretWord[letIndex] in lettersGuessed:
            secretWord_guess[letIndex] = secretWord_list[letIndex]
        letIndex += 1

    return "".join(secretWord_guess)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet[alphabet.index(letter)] = ""
    return "".join(alphabet)

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
    lettersGuessed = []
    totalGuesses = len(secretWord)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",str(len(secretWord)),"letters long.")
    while isWordGuessed(secretWord,lettersGuessed) == False:
        print("You have",str(totalGuesses),"guesses left.")
        print('Available letters:', getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:
            print('Oops! You have already guessed that letter!', secretWord_guess)
        else:
            # Call function to add letter to lettersGuessed
            if letter not in lettersGuessed:
                lettersGuessed.append(letter)
                print("Good guess!", getGuessedWord(secretWord,lettersGuessed))
            else:
                print('Oops. That letter is not in my word:', secretWord_guess)

    #print(getGuessedWord(secretWord,lettersGuessed))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
