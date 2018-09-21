'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''



# import random


# def guess():
#     player_guess = int(input("Guess a number: "))
#     num = random.randint(1,101)
#     while True:

#         if player_guess == num :
#             print("You Win!")
#             break
#         elif player_guess < num:
#             print("Guess Higher")
#         elif player_guess > num:
#             print("Guess Lower")
# print(guess())








import random
num = random.randint(1, 100)
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('Congrats, you win!')
        break
    elif i < num:
               print('Guess Higher')
    elif i > num:
               print('Guess Lower')




