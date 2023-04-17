# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 19:21:35 2022

@author: Rowan
"""

a = 'hannah'


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    perms = []
    all_perms = []
    all_perms_no_dupes = []
    n = len(sequence)
    if n == 1:
        perms.append(sequence)
        return perms
    else:
        perms = get_permutations(sequence[1:])
        for item in perms:
            for i in range(n):
                if i == 0:
                    all_perms.append(sequence[0] + item)
                elif i == n-1:
                    all_perms.append(item + sequence[0])
                else:
                    all_perms.append(item[:i] + sequence[0] + item[i:])
        [all_perms_no_dupes.append(piece) for piece in all_perms if piece not in all_perms_no_dupes]
        return all_perms_no_dupes 
        
        
print(get_permutations(a))