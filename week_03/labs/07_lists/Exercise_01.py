'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''

def user_sum(l):
    sum = 0
    for n in l:
        sum += n
    print(sum)

print(user_sum([1,2,3,4,5,6,7,8,9,10]))
