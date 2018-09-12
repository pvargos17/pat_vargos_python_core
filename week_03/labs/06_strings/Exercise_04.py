'''
Write a script that finds the first vowel in a a user inputted string.

'''
def first_vowel(s):
    vowels = "aeiou"
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            return i
            break

print first_vowel("patrick")
