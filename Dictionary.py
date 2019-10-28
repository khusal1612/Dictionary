import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "Please check the entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter Word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print('Translation: ')
    print(output)
