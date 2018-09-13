'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''

input_l=[1,2,3,4,5,6,7,8,9]
new_tupple = []
def make_tuple(l):
    l.sort()
    for i in range(0, len(l), 2):
        list_slice = l[i:i+2]
        if len(list_slice) % 2 != 0:
            list_slice.append(0)
        tuple_1 = tuple(list_slice)
        new_tupple.append(tuple_1)
        print(tuple_1)
    return new_tupple

print(make_tuple(input_l))




#
