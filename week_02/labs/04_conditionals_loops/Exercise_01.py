'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''

num = int(input("Enter a number between 1 and 1,000,000,000: "))
while num != 0:
    if num % 2 == 0:
        print ("Even", num)
    else:
        print("Odd", num)
