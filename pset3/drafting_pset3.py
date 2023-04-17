# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:23:23 2022

@author: rowbi


words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
         ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
         ("fork", 7):209, ("FORK", 4):308}

for (word,n) in words.keys():
    print(word,n)
    print (len(word))
    #print(stri, n)
    print(words[(word,n)])"""
    
SCRABBLE_LETTER_VALUES = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = str.lower(word)
    score = 0
    len_score = 7*len(word) - 3*(n-len(word))
    for i in word:
        if i in SCRABBLE_LETTER_VALUES:
            score = score + SCRABBLE_LETTER_VALUES[i]
    if len_score > 1:
        score = score*len_score
    return score
    #pass  # TO DO... Remove this line when you implement this function
    
    
print(get_word_score("bought", 6))


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    for i in word:
        if i in hand.keys():
            new_hand[i] -= 1
    pass  # TO DO... Remove this line when you implement this function

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# check each letter in the word against each letter in the hand, if
# a given letter in the word is in the hand, then remove that letter from the hand.
# note however that the original hand must stay the same so we need to copy the
# original hand and then operate on that one

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    new_hand = hand.copy()
    for i in word:
        if new_hand[i] > 0:
            new_hand[i] -= 1
        else:
            return False
    if word in word_list:
        return True
            
            
            

    pass  # TO DO... Remove this line when you implement this function