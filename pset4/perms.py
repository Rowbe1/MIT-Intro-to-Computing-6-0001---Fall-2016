#-*-coding:utf8;-*-
#qpy:console

#print ("This is console module")

letters = 'rowaboyles'
#nn = len(letters)
#for i in range(nn):
    #print(i)

def find_perms(seq):

    perms = []
    all_perms = []
    n = len(seq)
    if n == 1:
        perms.append(seq)
        #print(perms)
        return perms
    else:
        perms = find_perms(seq[1:]) #reduce sequence down to single letter
        for item in perms: #for each letter
            for i in range(n): #for every positioon in the sequence
                #print(all_perms)
                if i == 0: #at first position in sequence
                    all_perms.append(seq[0] + item) #bring letter to intial position
                elif i == n-1: #at last position in sequence
                    all_perms.append(item + seq[0]) #bring letter to the end
                else: 
                    all_perms.append(item[:i] + seq[0] + item[i:]) #put letter in the indexed position
        return all_perms  
        
print(find_perms(letters))
                   
                
                
                
            
        

        
    