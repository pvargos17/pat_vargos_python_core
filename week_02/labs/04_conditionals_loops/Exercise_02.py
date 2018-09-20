'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''



def day_counter():
    num = int(input("Please enter a numer: "))
    if num == 1:
       return print("Sunday")
    elif num == 2:
        return print("Monday")
    elif num == 3:
        return print("Tuesday")
    elif num == 4:
        return print("Wednesday")
    elif num == 5:
        return print("Thursday")
    elif num == 6:
        return print("Friday")
    elif num == 7:
        return print("Saturday")
    else:
        return print("other")


print(day_counter())



# user_pick = int(input("Enter a number: "))

# if user_pick not in [1, 2, 3, 4, 5, 6, 7]:
#     print("Other")
# elif user_pick == 1:
#     print("Monday")
# elif user_pick == 2:
#     print("Tuesday")
# elif user_pick == 3:
#     print("Wednesday")
# elif user_pick == 4:
#     print("Thursday")
# elif user_pick == 5:
#     print("Friday")
# elif user_pick == 6:
#     print("Saturday")
# else:
#     print("Sunday")
