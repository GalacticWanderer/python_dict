import json  # library to work with json


# mehtod to find a value for a given key
def findADef():
    word = input("Enter a word: ")
    word = word.lower()  # converting input to lower case
    try:
        data = json.load(open("data.json"))  # loading the data.json file
        return data[word]  # returning the value associated with the key
    except KeyError:
        return "Word doesn't exist"  # return this if key don't exist


print(findADef())  # dadadadada adada
