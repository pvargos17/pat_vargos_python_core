'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''

upper = int(input("Please enter uppbound: "))
lower = int(input("Please enter lowerbound: "))

def square():
    for i in range(lower, upper+1):
        print(i**2)
print(square())




# lower, upper = input("Enter lower and upper bound (both inclusive), \
# separated by a space: ").split()

# for n in range(int(lower), int(upper)+1):
#     print(n**2)
