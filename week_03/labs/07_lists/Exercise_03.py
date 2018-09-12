'''
Complete Exercise 10.1 (p.100) from the textbook.

Sum up all elements from a nested list of integers.

'''
t = [[1,2],[3],[4,5,6]]

def nest_sum(l):
    new_list = []
    totals = 0
    for i in l:
        for j in i:
            new_list.append(j)
    totals=sum(new_list)
    print(totals)
print(nest_sum(t))

