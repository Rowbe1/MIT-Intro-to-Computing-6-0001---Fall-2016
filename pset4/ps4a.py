# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

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

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'dog'
    print('Input:', example_input)
    print('Expected Output:', ['dog', 'odg', 'ogd', 'dgo', 'gdo', 'god'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'bug'
    print('Input:', example_input)
    print('Expected Output:', ['bug', 'ubg', 'ugb', 'bgu', 'gbu', 'gub'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'app'
    print('Input:', example_input)
    print('Expected Output:', ['app', 'pap', 'ppa'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #pass #delete this line and replace with your code here

