# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 19:14:32 2022

@author: Rowan
"""
import string
a = string.ascii_lowercase
A = string.ascii_uppercase
shift = 12
shift_lift = shift
dicto = {}
DICTO = {}
listo = []
lista = []
twist = []
twista = []
listy = []
n = 1
N = 1

for i in a:
    dicto[n] = i
    n += 1
for i in A:
    DICTO[N] = i
    N += 1
print('lower case letters dict:', dicto)
print('upper case letters dict:', DICTO)

for i in a:
    listo.append(i)
print('list of lower case letters', listo)

for i in A:
    lista.append(i)
print('list of upper case letters', lista)

while shift_lift < 27:
    listy.append(shift_lift)
    shift_lift += 1
print('shifting the index:', listy)

shift_lift = 1

while shift_lift < shift:
    listy.append(shift_lift)
    shift_lift += 1
print('shifted index:', listy)


for item in listy:
    twist.append(dicto.get(item))
    twista.append(DICTO.get(item))
print('shifted letters (lower):', twist)
print('shifted letters (upper):', twista)
    
dictat = {}
dictata = {}

for i in listo:
    dictat[i] = ''
print('lower case dict (again):', dictat)

n = 0
for item in dictat:
    dictat[item] = twist[n]
    n += 1
print('full shifted lower case dict:', dictat)
    
for i in lista:
    dictata[i] = ''
print('upper case dict (again):', dictata)

n = 0
for item in dictata:
    dictata[item] = twista[n]
    n += 1
    
print('full shifted upper case dict:', dictata)

dictat.update(dictata)
print(dictat)
    

message = 'I am a newbie but I like to strike OUT! Gimme 5 minutes and I\'ll chat your ear off. Thanks'

new_message = ''
for item in message:
    if item in dictat:
        new_message = new_message + dictat[item]
    else:
        new_message = new_message + item

print(new_message)

    
