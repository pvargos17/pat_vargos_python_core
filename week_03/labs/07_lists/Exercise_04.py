'''
Complete Exercise 10.2 (p.100) from the textbook.

'''
t = [1,2,3]

def cumsum(l):
    new_list = []
    for i in l:
        if i == l[0]:
            new_list.append(i)
        else:
            new_list.append(i + l[i-1])
    return (new_list)
print(cumsum(t))
