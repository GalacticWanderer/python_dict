import json  # library to work with json
from difflib import get_close_matches  # library for words matching ratio


# a helper loop to print out the word Definition
def loopHelper(word):
    i = 1
    for x in word:
        print("Definition %s: %s" % (i, x))
        i += 1


# mehtod to find a value for a given key
def findADef():
    word = input("Enter a word: ")
    word = word.lower()  # converting input to lower case
    data = json.load(open("data.json"))  # loading the data.json file

    # if exits, simply print value
    if word in data:
        loopHelper(data[word])
        return ""
    # if word exits as a title, simply print value
    elif word.title() in data:
        loopHelper(data[word.title()])
        return ""
    # if word exits as upper case, simply print value
    elif word.upper() in data:
        loopHelper(data[word.upper()])
        return ""
    # checking to see if there are any similar words
    elif len(get_close_matches(word, data.keys())) > 0:
        # giving the user a prompt to retry
        # word contains the first item on the list
        word = get_close_matches(word, data.keys())[0]
        response = input("Did you mean %s? enter y to confirm: " % word)
        # upon entering y, pass arg to loopHelper
        if response.lower() == 'y':
            loopHelper(data[word])
            return ""
        else:
            return "Word doesn't exist"
    else:
        return "Word doesn't exist"


print(findADef())
