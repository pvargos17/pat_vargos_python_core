'''
Complete Exercise 8.4 (p.80) from the textbook by writing out the docstrings for the functions.

'''
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1("jolly"))

def any_lowercase2(s):
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print(any_lowercase3("jolly"))


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

print(any_lowercase4("jolly"))


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True
print(any_lowercase5("jolly"))
