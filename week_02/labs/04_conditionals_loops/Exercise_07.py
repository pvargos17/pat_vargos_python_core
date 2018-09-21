'''
Use a "while" loop to print out every third number counting backwards from 1000 to 1.

'''


num = 1000
counter = 1
while num > 0:
    if counter == 3:
        print(num)
        counter = 1
    else:
        counter += 1
        num -= 1





# count = 1000
# counter = 1

# while count > 0:
#     if counter == 3:
#         print(count)
#         counter = 1
#     else:
#         counter += 1
#         count -= 1
