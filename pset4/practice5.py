# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:19:07 2022

@author: Rowan
"""

VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

#convert string to lowercase, check the string is 5 items long and only contains each item in vowels once
        #make dictionary with vowels first then consonants
        #pass the string to a variable
        #make an upper case version
        #convert the strings into a list
        #update the values of initial values in the dictionary (all vowels) with the lists

vowelie = 'oieau'
vowelie = vowelie.lower()
COMBINED_VOWELS = VOWELS_LOWER + VOWELS_UPPER
assert len(vowelie) == 5
for item in vowelie:
    if vowelie.count(item) > 1:
        raise ValueError('Repeated item, please input all 5 vowels')
for item in vowelie:
    if item not in VOWELS_LOWER:
        raise ValueError('Please enter only vowels')
VOWELIE = vowelie.upper()
transpose_vowels = []
for item in vowelie:
    transpose_vowels.append(item)
for item in VOWELIE:
    transpose_vowels.append(item)
    
print(transpose_vowels)
transpose_dict = {}
for item in VOWELS_LOWER:
    transpose_dict[item] = item
for item in VOWELS_UPPER:
    transpose_dict[item] = item
for item in CONSONANTS_LOWER:
    transpose_dict[item] = item
for item in CONSONANTS_UPPER:
    transpose_dict[item] = item

n = 0
for item in COMBINED_VOWELS:
        transpose_dict[item] = transpose_vowels[n]
        n += 1


print(transpose_dict)    
    
print(vowelie)
