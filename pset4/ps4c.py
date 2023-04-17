# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
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

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
        

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        self.valid_words_copy = self.valid_words[:]
        return self.valid_words_copy
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        #intialise variables
        self.vowels_permutation = vowels_permutation.lower()
        COMBINED_VOWELS = VOWELS_LOWER + VOWELS_UPPER
        transpose_dict = {}
        transpose_vowels = []
        VOWELS = vowels_permutation.upper()
        
        #error checking - only 5 characters, all vowels, not repeated
        assert len(vowels_permutation) == 5
        for item in vowels_permutation:
            if vowels_permutation.count(item) > 1:
                raise ValueError('Repeated item, please input all 5 vowels')
        for item in vowels_permutation:
            if item not in VOWELS_LOWER:
                raise ValueError('Please enter only vowels')
        
        #generate list of transposed vowels in sequence
        for item in vowels_permutation:
            transpose_vowels.append(item)
        for item in VOWELS:
            transpose_vowels.append(item)
        
        #make dictionary of all letters, vowels first in normal order, lower then uppercase
        for item in VOWELS_LOWER:
            transpose_dict[item] = item
        for item in VOWELS_UPPER:
            transpose_dict[item] = item
        for item in CONSONANTS_LOWER:
            transpose_dict[item] = item
        for item in CONSONANTS_UPPER:
            transpose_dict[item] = item
        
        #update values of vowels in dictionary to those from tranposed list
        n = 0
        for item in COMBINED_VOWELS:
                transpose_dict[item] = transpose_vowels[n]
                n += 1
        
        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        self.transpose_dict = transpose_dict
        new_message = '' #initialise blank message
        for item in self.message_text: #for every character in the message
            if item in transpose_dict: #if the character is in the dictionary
                new_message = new_message + transpose_dict[item] #add that character's dictionary value (i.e. transposed character) to the message
            else:
                new_message = new_message + item #otherwise just add the character to the message (i.e. punctuation etc)
        return new_message #encrypted message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        #generate list of all permutations of vowels using function from part a
        perms = get_permutations(permutation)
        
        perm_scores = {} #initialise dictionary to compare best permutations of vowels for decryption
        for item in perms: #for every permutation of vowels
            perm_scores[item] = 0 #add the permutation to the score dictionary and set value to zero
            words = [] #reinitialise a list of words to be generated by this permutation
            temp_dict = SubMessage.build_transpose_dict(self, item) #generate a temporary dictionary using this permutation of vowels
            temp_message = SubMessage.apply_transpose(self, temp_dict) #use the dictionary to decrypt the message (encrypt the encryption)
            words.extend([item for item in temp_message.split(' ')]) #split the encrypted message into individual words and add the word list
            for val in words: #for each word in the new word list
                if is_word(self.valid_words, val): #if the word is valid, i.e. it is in the list of valid words
                    perm_scores[item] +=1 #increase the score for the permutation used, increase the value of that key by 1 in the dictionary of scores
        best_perm = max(perm_scores, key=perm_scores.get) #obtain the key with the highest score 
        
        if perm_scores[best_perm] > 0: #if there is a permutation that generated valid words
            best_dict = SubMessage.build_transpose_dict(self, best_perm) #generate the transposition dictionary from that key
            best_message = SubMessage.apply_transpose(self, best_dict) #generate the decrypted message using that dictionary
            return best_message
        else:
            return self.message_text
                    
            
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    message = SubMessage("Wassup homies, right about now I be up in this biatch. Whassthashiznach? Funking be punkin and outside influences be jumpin right up in the spot. Hit me up sometime boyee")
    permutation = "eoaui"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "How the fuck should I know")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())