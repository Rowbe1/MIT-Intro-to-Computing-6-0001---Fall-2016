#-*-coding:utf8;-*-
#qpy:console

print ("This is console module")

import string

a = string.ascii_lowercase
lowercase = list(a)
shifted = []
shift = 3
shifted_dict = {}

for i in range(shift,len(lowercase)):
    shifted.append(lowercase[i])
for i in range(shift):
    shifted.append(lowercase[i])
    
print(shifted)  

n = 0
for i in lowercase:
    shifted_dict[i] = shifted[n]
    n += 1

print(shifted_dict)


