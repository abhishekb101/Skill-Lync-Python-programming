"""
Contains methods that allow the smooth running of the
Application and support the main logic loop operation. 
"""
import json
import os 


def preprocessed(string):
    """
    Removes punctuation marks and any trailing spaces from the input string
    and returns the preprocessed string
    """
    #Selecting these from the keyboard -- Includes digits as well
    punc = '!@#$%^&*+=-_:[]{}()<>\/|"";,.~`?0123456789' 
    
    #Removing the leading and trailing spaces along with converting to lower case
    string_lower = string.strip().lower()
    
    #Creating a string to eliminate the punc characters
    clean = ''
    
    #Iterating over the characters in original string and checking whether they are a punctuation or not
    for char in string_lower:
        if char not in punc:
            clean += char
            
    return clean


def dummy_dict(file_name = 'words.txt'):
    """
    Taking the dummy english dict and loads it in 
    json dict format into the file words.txt
    for starting the application
    """
    #Creating a dummy english dict to start the English dictionary application
    english_dict = {'Abbreviate' : 'shorten',
                'Abhorrence' : 'Disgust',
                'Abolish' : 'Put an end to',
                'Absolve' : 'Set free from blame',
                'Accord' : 'Agreement',
                'Acumen' : 'Insight',
                'Bachelor' : 'Unmarried man',
                'Backlash' : 'violent',
                'Backwater' : 'secluded, or dull place',
                'Bamboozle' : 'Mystify',
                'Banter' : 'Good-humoured teasing.',
                'Cupidity' : 'Greed', 
                'Curb' : 'check or restraint', 
                'Cyclic' : 'Recurring in circles',
                'Decade' : 'Period of ten years',
                'Decimate' : 'destroy a large proportion of.',
                'Eldest' : 'First born',
                'Eloquent' : 'Expressive',
                'Emboss' : 'Carve or decorate with a design in relief.', 
                'Fodder' : 'Animal food',
                'Foregoing' : 'preceding',
                'Grapple' : 'fight in close combat',
                'Grieve' : 'suffer grieve',
                'Hamlet' : 'a small village',
                'Haughty' : 'Arrogant',
                'Illicit' : 'Unlawful',
                'Impeach' : 'Charge with a crime against the state',
                'Jollity' : 'festivity', 
                'Jurist' : 'Expert in law'}
    
    #Preprocessing the dummy entries and storing into a cleaned_dict
    cleaned_dict = {}
    
    #Iterating over the keys and values of the dict and preprocessing them
    for word, meaning in english_dict.items():
        up_word = preprocessed(word)
        up_meaning = preprocessed(meaning)
        
        #Storing them in the new dictionary
        cleaned_dict[up_word] = up_meaning    
    
    #Using the append operation to add the dummy dict
    with open(file_name, 'a') as file:
        
        #Adding the 
        json.dump(cleaned_dict, file)


def add_newword(cleaned_word, cleaned_meaning, file_name = 'words.txt'):
    """
    Takes the preprocessed word, its meaning and default txt file argument as input.
    Updates the txt file with the temporary dict containing word and meaning as key:value pair.
    Also, handles the condition where the file doesn't exist or contains no serialised data
    """
        
    #Storing it into a temporary dict to append to the file above
    tmp = {cleaned_word : cleaned_meaning}

    #Checking whether the above file_name exists or not -- To append the dict to it
    if os.path.isfile(file_name):

        #Above file already exists -- append the tmp dict in the file
        #Opening the file in 'r+' mode for reading and writing simultaneously
        with open(file_name, 'r+') as file:

            #Loading the data from the file using json.load
            data = json.load(file)
            
            #Checking whether the cleaned_word is part of the english dictionary or not
            #Only allow when word if it is not already present
            if cleaned_word in data.keys():
                
                #Handling the condition where word is already present in dictionary and this is a redundant task

                print("\033[1m" + '\nThe word "{}" is already present in the dictionary.'.format(cleaned_word) + "\033[0m")
                print("\033[1m" + 'Returning back to the main menu...' + "\033[0m")
                
                #Printing a boundary to act as separator
                print('\n' + '-x-' * 30)
            
            else: 
                #Appending the tmp dict into data
                data.update(tmp)

                #Reverting the cursor of the file to 0 (Original position)
                file.seek(0)

                #Writing the data file object back into the file using concept of serialisation
                json.dump(data, file)

                #Printing a message when the data is successfully stored in words.txt
                print("\033[1m" + '\nThe word "{}" and its meaning "{}" have been successfully stored !!\n'.format(cleaned_word,
                                                                                        cleaned_meaning) + "\033[0m")
                #Printing a boundary to act as separator
                print('\n' + '-x-' * 30)

    #Logic when the file does not exist or doesn't contain any data in it
    else:
        
        #Opening the file in appending mode to handle both scenarios above
        file = open(file_name, 'a')

        #Writing the temporary dict as a json object into the file 
        json.dump(tmp, file)

        #Closing the file
        file.close()

        #Printing the message when file and data has been successfully added
        print("\033[1m" + '\nThe word "{}" and its meaning "{}" was added to the file.'.format(cleaned_word,
                                                                                       cleaned_meaning) + "\033[0m" ) 
        print("\033[1m" + 'Continue adding words to build dictionary !!' + "\033[0m")
        
        #Printing a boundary to act as separator
        print('\n' + '-x-' * 30)
    
    
def find_meaning(cleaned_word, file_name = 'words.txt'):
    """
    Taking the preprocessed word as input and returning its meaning if it is found in the
    English dictionary file. Displaying an apt message when it isn't found
    """
    
    #Checking whether the file exists or not -- As we are also addressing the case when the English dictionary
    #has not been created and this is the first option entered
    if os.path.isfile(file_name):
        
        #Opening the file in read mode
        with open(file_name, 'r') as file:
            
            #Loading the json dict object stored in the dictionary as data variable
            data = json.load(file)
            
            #Checking whether the word is present or not in the dictionary already
            if cleaned_word in data:
                print("\033[1m" + '\nThe word "{}" is present in the the dictionary.'.format(cleaned_word) + "\033[0m" )
                print("\033[1m" + 'The meaning of "{}": {}'.format(cleaned_word, data[cleaned_word]) + "\033[0m")
                
                #Printing a boundary to act as separator
                print('\n' + '-x-' * 30)
                
            else:
                print("\033[1m" + '\nThe word "{}" is not present in the dictionary.'.format(cleaned_word) + "\033[0m")
                print("\033[1m" + 'Returning back to the main menu...' + "\033[0m")
                
                #Printing a boundary to act as separator
                print('\n' + '-x-' * 30)
    
    #Handling the situation where the file doesn't exist
    else:
        print('\nThe file does not exist. Either create a file or Select option 1 to add new words.')
        print('Returning to the main menu...')   
        
        #Printing a boundary to act as separator
        print('\n' + '-x-' * 30)

        
def update_word(cleaned_word, file_name = 'words.txt'):
    """
    Accepts a word which is already present in the english dictionary 
    and updates its meaning. If not present, it returns to the main menu
    """

    #Checking whether the file exists or not -- As we are also addressing the case when the English dictionary
    #has not been created and this is the first option entered
    if os.path.isfile(file_name):
        
        #Opening the file in read mode
        with open(file_name, 'r') as file1:
            
            #Loading the json dict object stored in the dictionary as data variable
            data = json.load(file1)
            
            #Checking whether the cleaned_word is part of the english dictionary or not - Only allow updation 
            if cleaned_word in data.keys():
                
                #Accepting the new meaning form the user and preprocessing it
                new_meaning = preprocessed(input('Enter the updated meaning for the word: '))
                
                #Updating the english dictionary data with this value
                data[cleaned_word] = new_meaning
            
            #Handling the condition where word is not present in dictionary to update its meaning
            else:
                print("\033[1m" + '\nThe word "{}" is not present in the dictionary.'.format(cleaned_word) + "\033[0m")
                print("\033[1m" + 'Returning back to the main menu...' + "\033[0m")
                
                #Printing a boundary to act as separator
                print('\n' + '-x-' * 30)
                
        #Updating the english dictionary into the file_name using json.dump method -- Allowing both write and read 
        with open(file_name, 'w+') as file2:
            
            #No changes to the dictionary in situations where cleaned_word is not present already
            json.dump(data, file2)
            
            #Starting from the start of the file
            file2.seek(0)
            
            #Loading the json string object as a dict object using json.load method
            data2 = json.load(file2)
            
            #Again checking whether the cleaned_word is in dictionary or not
            if cleaned_word in data2.keys():
                print("\033[1m" + '\nThe word "{}" is present in the the dictionary.'.format(cleaned_word) + "\033[0m")
                print("\033[1m" + '\nThe meaning of word "{}" has been changed to: {}'.format(cleaned_word,
                                                                              data2[cleaned_word]) + "\033[0m")
                
                #Printing a boundary to act as separator
                print('\n' + '-x-' * 30)

    
    #Handling the situation where the file doesn't exist
    else:
        print("\033[1m" + '\nThe file does not exist. Either create a file or Select option 1 to add new words.'+ "\033[0m")
        print("\033[1m" + 'Returning to the main menu...' + "\033[0m")
        
        #Printing a boundary to act as separator
        print('\n' + '-x-' * 30)