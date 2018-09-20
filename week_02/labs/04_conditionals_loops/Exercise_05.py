'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''


def u_d_sum():
    upper = int(input("Please enter an upperbound: "))
    downer = int(input("Please enter a lowerbound: "))
    average = (upper - downer)/2
    counter = 0
    for i in range(downer, upper + 1):
            counter += i

    print(counter)
    print(average)

print(u_d_sum())








# user_numbers = (int(input("upper bound", "lower bound")))
# average = ((lower bound + upper bound) / 2)
# for i in user_numbers:
#     if i > {}.format(lowerbound):
#     sum += ({} + {}).format(lower bound, lower bound +1)
# else:
#     print(sum)
#     print(average)


