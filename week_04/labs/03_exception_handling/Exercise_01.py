'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
while True:
    try:
        check_int = int(input('Please input a number: '))
        print(check_int)
        #if type(check_int) == int
        break
    except ValueError:
        print('Not an integer, please input an integer: ')
print("Thank you!")

