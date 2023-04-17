# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 16:38:47 2022

@author: Rowan
"""

import string
punc = string.punctuation
print(punc)

a = 'jeepers creepers! where\'d you  get those eyes?!'
for item in punc:
    a = a.replace(item,' ')
print(a)

listle = []
for item in a.split():
    listle.append(item)
print(listle)


c = ' '
listle1 = c.join(listle)
print(listle1)

j = ['tees', 'balls', 'jocks', 'back end']



d = c.join(j)

print(d)

e = 'jeepers creepers'

print(e in a)
