'''
Write a script that takes a user inputed string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''

def all_caps_lower_vowels(s):
    print (s.upper())
    print (s.lower())
    vowels = "aeiou"
    camel = ""
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            camel += i.lower()
        elif i != "a" or i == "e" or i == "i" or i == "o" or i == "u":
            camel += i.upper()
    print(camel)



print(all_caps_lower_vowels("patrick"))

