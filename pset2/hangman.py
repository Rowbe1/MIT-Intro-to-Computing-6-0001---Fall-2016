# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    if secret_word == letters_guessed:
        return True
    else:
        return False
    


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    current__guess = ''
    for i in secret_word:
        if i in letters_guessed:
            current__guess += str(i)
        else:
            current__guess += '_ '
    letters_guessed = current__guess
    return letters_guessed



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_available = ''
    for i in string.ascii_lowercase:
        if i in letters_guessed:
            letters_available = letters_available
        else:
            letters_available += i         
    return letters_available
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    consonants = 'bcdfghjklmnpqrstvxyz'
    letters_guessed = ''
    print('Welcome to the game Hangman!\n I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')   
    while guesses > 0:
        if is_word_guessed(secret_word, str(get_guessed_word(secret_word, letters_guessed))) == False:
            print('You have ' + str(guesses) + ' guesses left.')
            print('You have ' + str(warnings) + ' warnings left.')
            print('Available letters: ' + str(get_available_letters(letters_guessed)))
            letter_guess = str(input('Please enter a letter: '))
            while str.isalpha(letter_guess) != True and guesses > 0:
                warnings -= 1
                print('Oops! That is not a valid letter. You have ' + str(warnings) + ' warnings left.')
                if warnings == 0:
                    print('For failing to heed the warning, you have lost a guess')
                    guesses -= 1
                    warnings = 3
                letter_guess = str(input('Please enter a letter: '))
            letter_guess = str.lower(letter_guess)
            if str(letter_guess) in str(secret_word) and str(letter_guess) not in str(letters_guessed):
                letters_guessed = letter_guess + get_guessed_word(secret_word, letters_guessed)
                print('Good guess ' +  str(get_guessed_word(secret_word, letters_guessed)))
            elif str(letter_guess) in str(secret_word) and str(letter_guess) in str(letters_guessed):
                print('Oops! You already picked that one ' + str(get_guessed_word(secret_word, letters_guessed)))
                warnings -= 1
                if warnings == 0:
                    print('For failing to heed the warning, you have lost a guess')
                    guesses -= 1
                    warnings = 3
            else:
                print('Oops, that one ain\'t in the word ' + str(get_guessed_word(secret_word, letters_guessed)))
                if str(letter_guess) in consonants:
                    guesses -= 1
                else:
                    guesses -= 2
        else:
            Total_score = guesses * len(secret_word)
            print('-----------------------\nCongrats! You guessed it\nYour total score is: ' + str(Total_score))
            return
    print('-----------------------\nYou have run out of guesses! Unlucky dude :(\nThe secret word was: ' + str(secret_word))
      
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')
    my_word_list = list(my_word)
    other_word_list = list(other_word)
    if len(my_word_list) == len(other_word_list):
        for index, item in enumerate(my_word_list): #could I have done: for i in range(len(word_list)) OR for i in word_list:??
            if item == '_':
                other_word_list[index] = '_'
    else:
        return False
    ''.join(other_word_list)
    ''.join(my_word_list)
    if my_word_list == other_word_list:
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ''
    for item in wordlist:
        if match_with_gaps(my_word, item) == True:
            possible_matches = possible_matches + item + '  '
    return possible_matches



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    consonants = 'bcdfghjklmnpqrstvxyz'
    letters_guessed = ''
    print('Welcome to the game Hangman!\n I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.\n Enter * to get a hint at any time')   
    while guesses > 0:
        if is_word_guessed(secret_word, str(get_guessed_word(secret_word, letters_guessed))) == False:
            print('You have ' + str(guesses) + ' guesses left (vowels cost 2 guesses)')
            print('You have ' + str(warnings) + ' warnings left.')
            print('Available letters: ' + str(get_available_letters(letters_guessed)))
            letter_guess = str(input('Please enter a letter: '))
            while str.isalpha(letter_guess) != True and guesses > 0 and letter_guess != '*':
                warnings -= 1
                print('Oops! That is not a valid letter. You have ' + str(warnings) + ' warnings left.')
                if warnings == 0:
                    print('For failing to heed the warning, you have lost a guess')
                    guesses -= 1
                    warnings = 3
                letter_guess = str(input('Please enter a letter: '))
            letter_guess = str.lower(letter_guess)
            if str(letter_guess) == '*':
                print('Possible word matches are: ' + show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            elif str(letter_guess) in str(secret_word) and str(letter_guess) not in str(letters_guessed):
                letters_guessed = letter_guess + get_guessed_word(secret_word, letters_guessed)
                print('Good guess ' +  str(get_guessed_word(secret_word, letters_guessed)))
            elif str(letter_guess) in str(secret_word) and str(letter_guess) in str(letters_guessed):
                print('Oops! You already picked that one ' + str(get_guessed_word(secret_word, letters_guessed)))
                warnings -= 1
                if warnings == 0:
                    print('For failing to heed the warning, you have lost a guess')
                    guesses -= 1
                    warnings = 3
            else:
                print('Oops, that one ain\'t in the word ' + str(get_guessed_word(secret_word, letters_guessed)))
                if str(letter_guess) in consonants:
                    guesses -= 1
                else:
                    guesses -= 2
        else:
            Total_score = guesses * len(secret_word)
            print('-----------------------\nCongrats! You guessed it\nYour total score is: ' + str(Total_score))
            return
    print('-----------------------\nYou have run out of guesses! Unlucky dude :(\nThe secret word was: ' + str(secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
