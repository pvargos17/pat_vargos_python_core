'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''


dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}


def combine_dict(a,s,d):
    new_dict = {}
    for c in a:
        new_dict[c] = a[c]
    for c in s:
        new_dict[c] = s[c]
    for c in d:
        new_dict[c] = d[c]
    print(new_dict)

    for k, v in new_dict.items():
        print(k, v)


print(combine_dict(dict_1,dict_2,dict_3))

