'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

# remember: range() also creates a generator object (try printing it!)
nums = range(1, 1000000)

gen = (print(n) for n in nums if (n % 1111 == 0))

for n in gen:
    n

