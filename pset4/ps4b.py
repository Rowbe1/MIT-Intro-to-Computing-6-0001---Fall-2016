# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
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

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        self.shift = shift
        assert 0 <= self.shift < 26 #check that the shift number is valid. Needs to be less than number of letters in alphabet and greater than zero
        a = string.ascii_lowercase #generate a string of lowercase letters
        A = string.ascii_uppercase #generate a string of uppercase letters
        lowercase = list(a) #turn the string of letters into a list (could combine this command and the above one)
        uppercase = list(A) #as for above
        shifted = [] #initialise list for shifted letters
        SHIFTED = [] #as above for uppercase
        shifted_lowers = {} #dictionary for shifted letters
        shifted_uppers = {} #as above for uppercase

        for i in range(self.shift,len(lowercase)): #for each item in the list of lowercase letters, starting with the index corresponding to the shift value and continuing to the end
            shifted.append(lowercase[i]) #add those tems to the shifted list
        for i in range(self.shift): #for each item in list of lowercase, starting at the start and ending at the index corresponding to the shift value
            shifted.append(lowercase[i]) #add those items to the shifted list - 
            
        for i in range(self.shift,len(uppercase)): #as above but for uppercase
            SHIFTED.append(uppercase[i])
        for i in range(self.shift):
            SHIFTED.append(uppercase[i]) 

        n = 0 #initialise n
        for i in lowercase: #for each character in the lowercase list
            shifted_lowers[i] = shifted[n] #create a key in the shifted dictionary corresponding to the character and set its value to that of the shifted list
            n += 1
        
        n = 0
        for i in uppercase:
            shifted_uppers[i] = SHIFTED[n] #as above but for uppercase
            n += 1
        
        shifted_lowers.update(shifted_uppers) #add uppercase dictionary to lower
        return shifted_lowers #return final dictionary

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #for full comments see "apply transpose" in ps4c
        self.shift = shift
        new_message = ''
        shifted_dict = Message.build_shift_dict(self, self.shift)
        for item in self.message_text:
            if item in shifted_dict:
                new_message = new_message + shifted_dict[item]
            else:
                new_message = new_message + item
        return new_message

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.encryption_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encryption_dict_copy = self.encryption_dict.copy()
        return encryption_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert 0 <= shift < 26
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        #for full comments see "decrypt message" in ps4c - only slight differences
        shift_scores = {}
        for i in range(26):
            shift_scores[i] = 0    
        shift_message = ()
        for i in range(26):
            words = []
            temp_decrypt = Message.apply_shift(self, i)
            words.extend([item for item in temp_decrypt.split(' ')])
            for item in words:
                if is_word(self.valid_words, item):
                    shift_scores[i] += 1
        best_shift = max(shift_scores, key=shift_scores.get)
        shift_message = (best_shift, Message.apply_shift(self, best_shift))
        return shift_message
        

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print(plaintext.get_message_text())
    print('Expected Output: jgnnq')
    print(plaintext.get_shift())
    print(plaintext.get_encryption_dict())
    plaintext.change_shift(5)
    print(plaintext.get_shift())
    print(plaintext.get_message_text_encrypted())
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    
    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('Having a good time is mandatory', 4)
    print('Expected Output: unknown')
    #print(PlaintextMessage.get_shift)
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('Lezmrk e kssh xmqi mw qerhexsvc')
    print('Expected Output:', (22, 'Having a good time is mandatory'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    story = get_story_string()
    ciphertext = CiphertextMessage(story)
    print(ciphertext.decrypt_message())