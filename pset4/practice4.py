# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:37:47 2022

@author: Rowan
"""

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


text = 'i am a new person, made great by the shoals of the afflicted, having opened up...blah, blah, blah...'

  
wordlist = load_words('words.txt')

little_wordlist = []


little_wordlist.extend([word.lower() for word in text.split(' ')])

print(little_wordlist)
