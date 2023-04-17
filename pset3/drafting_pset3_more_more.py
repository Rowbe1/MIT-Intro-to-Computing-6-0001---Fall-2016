# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:29:45 2022

@author: Rowan
"""
import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    #look for letter in hand
    letter = letter.lower() 
    if letter in hand.keys() and letter != '*':
        letter_num = hand[letter]
        del hand[letter]
        if letter in VOWELS:
            for i in range(letter_num):
                x = random.choice(VOWELS)
                hand[x] = hand.get(x, 0) + 1
        elif letter in CONSONANTS:
            for i in range(letter_num):
                x = random.choice(CONSONANTS)
                hand[x] = hand.get(x, 0) + 1
    else:
            print("letter not in hand")  
    return hand
   
hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
letter = 'f'
#print(len(letter))
#print(letter == str)
#print(len(letter) == 1)
print(substitute_hand(hand, letter))
x = 0
for i in hand.keys():
    x += hand[i]

print(hand)
print(x)
