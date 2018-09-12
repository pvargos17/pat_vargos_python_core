'''
Complete Exercise 10.3 (p.100) from the textbook.

'''
t=[1,2,3,4,5,6]

def middle(l):
    if len(l) <= 2:
        return "No Middle"
    else:
        return l[1:-1]
print(middle(t))
