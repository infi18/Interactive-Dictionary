import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def defi(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Sorry did you mean %s ?? Enter Y for yes and N for no: " %get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Sorry !! The word does not exist in the dictionary"
        else:
            return "Sorry we didn't understand your query please try again :)"
    else:
        return "Sorry !! The word does not exist in the dictionary"

word = input("Enter a word: ")

output = (defi(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
