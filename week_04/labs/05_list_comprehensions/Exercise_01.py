'''
Use a one-line list comprehension to express the following functionality:

letters = []

for letter in 'suchalongword':
    letters.append(letter)

print(letters)

'''
letter = "suchalongword"

new_letters = [(n) for n in letter]
print(new_letters)
