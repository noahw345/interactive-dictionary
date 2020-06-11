import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data: #if user inputs word found in dictionary
        return data[w]
    elif w.title() in data: #if user inputs proper nouns like Paris
        return data[w.title()]
    elif w.upper() in data: #if user inputs acronyms such as USA
        return data[w.upper()] 
    elif len(get_close_matches(w, data.keys())) > 0: #if user inputs word wrong
        yn = input("Did you mean %s instead? Enter Y if so, or enter N if not: " % get_close_matches(w, data.keys())[0])
        if yn == "Y": #returns the closest matching word
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N": #notifies user that word doesn't exist in dictionary
            return "The word doesn't exist. Please double check your input."
        else: #if user doesnt input 'Y' or 'N'
            return "Please only enter Y or N."
    else: #if there are no similar words
        return "The word doesn't exist. Please double check your input."

while True:
    word = input("If you would like to exit, enter '\end', otherwise enter word: ")
    if(word != "\end"): #ends program if user enters sentinel value
        output = translate(word)
        if type(output) == list: #if definition is able to be returned, the list must be printed without brackets
            for item in output:
                print(item)
        else: 
            print(output)
    else:
        break