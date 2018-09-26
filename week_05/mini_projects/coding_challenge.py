

# list1 = [1,2,3]
# list2 = [1,2,6]

# def sum_of(list):
#     for i in range(len(list)-1):
#         for c in range(i +1, len(list)) :
#             if list[i] + list[c] == 8:
#                 return True
#     return False
# print(sum_of(list1))
# print(sum_of(list2))

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [1,2,6,3,9,2]
bubbleSort(alist)
print(alist)
