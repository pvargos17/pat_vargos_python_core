'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''
import random

def guesser():
    num = int(input("Please input number 0 - 1 00,000,00: "))
    while True:
        if num % 2 == 0:
            return (f"{num} is an even number!")
        elif num % 2 != 0:
            return (f"{num} is an odd number!")
        else:
            return ("0 is not even or odd!")

print(guesser())



# num = int(input("Enter a number between 1 and 1,000,000,000: "))
# while num != 0:
#     if num % 2 == 0:
#         print ("Even", num)
#     else:
#         print("Odd", num)
