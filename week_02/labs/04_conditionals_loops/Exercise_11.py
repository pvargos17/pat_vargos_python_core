'''
Apply a Cesar cipher of 7 to the 'secret' variable.

p.s.: http://www.montypython.net/scripts/dentist.php

'''

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7


message = input(secret)
number = input(7)
final_message = ""
for char in message:
    enumerated = ord(char)
    transformed = enumerated + number
    new_letter = chr(transformed)
    final_message += new_letter
print("Your encoded message is: ", final_message)

