"""Containing few functions to operate on a string effectively"""

def fun1(st1):
    """
    Taking a string as input and checking whether it is a palindrome or not
    """
    punc = '!@#$%^&*+=-_:[]{}()\/|"";,.?' 
    
    #Removing the leading and trailing spaces along with converting to lower case
    st_lower = st1.strip().lower().replace(' ','')
    
    #Creating a string to eliminate the punc characters
    cleaned_string = ''
    
    #Iterating over the characters in original string and checking whether they are a punctuation or not
    for char in st_lower:
        if char not in punc:
            cleaned_string += char
            
    rev = cleaned_string[::-1]
    
    #Iterating over the length of the string
    for idx in range(len(rev)): 
        if cleaned_string[idx] != rev[idx]:
            print("\nThe entered string '{}' is not a palindrome ".format(st1))
            break
    
    else:
        print("\nThe entered string '{}' is a palindrome".format(st1))
        
def fun2(st):
    """
    Takes a string as input and returns the number of unique characters in it
    """
    d = {}
    
    #Iterating over the characters in the string
    for char in st:
        
        #If the character is present in dictionary d
        if char in d:
            d[char] += 1
        
        #If character is not present in dictionary
        else:
            d[char] = 1
            
    print('\nThe number of unique characters in the entered string "{}": {}'.format(st, len(d)))
    
def fun3(st):
    """
    Given the string as input it calculates the length of the string
    """
    print('\nThe length of the string "{}": {}'.format(st, len(st)))