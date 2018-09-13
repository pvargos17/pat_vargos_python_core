'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''

def long_func(sent):
    new_dict = {}
    for char in sent:
        if char.isspace():
            pass
        elif char.isupper():
            new_dict["uppercase"] = new_dict.get("uppercase", 0) + 1
        elif char.islower():
            new_dict["lowercase"] = new_dict.get("lowercase", 0) + 1
        else:
            new_dict["punctuation"] = new_dict.get("punctuation", 0) + 1
    return (new_dict)

print(long_func("I love to work with dictionaries!"))
