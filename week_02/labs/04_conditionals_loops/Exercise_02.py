'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''
user_pick = int(input("Enter a number: "))

if user_pick not in [1, 2, 3, 4, 5, 6, 7]:
    print("Other")
elif user_pick == 1:
    print("Monday")
elif user_pick == 2:
    print("Tuesday")
elif user_pick == 3:
    print("Wednesday")
elif user_pick == 4:
    print("Thursday")
elif user_pick == 5:
    print("Friday")
elif user_pick == 6:
    print("Saturday")
else:
    print("Sunday")
