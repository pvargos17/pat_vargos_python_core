'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

_list=["dog", "cat", "snake"]


def my_enmerate(iterable):
    for i in range(len(iterable)):
        print(i, iterable[i])
print(my_enmerate(_list))
