'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.

Solution: http://thinkpython2.com/code/has_duplicates.py.

Source: Chapter "Dictionaries" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2011.html

'''

def has_duplicates(l):
    new_dict = {}
    for x in l:
        if x in new_dict:
            return True
        new_dict[x] = "Duplicate"
    return False

p = ["baseball", "football", "basketball", "baseball"]
v = ["baseball", "football", "basketball"]

print(has_duplicates(p))
print(has_duplicates(v))
