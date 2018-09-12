'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]
new_list = []
def common_numbers(list1, list2):
    for n in list_one:
        if n in list_two:
            new_list.append(n)
    print(new_list)

print(common_numbers(list_one,list_two))

