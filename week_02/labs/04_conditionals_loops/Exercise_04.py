'''
Print out every prime number between 1 and 100.

'''
for i in range(1, 101):
    if (i == 2) or (i == 3) or (i == 5) or (i == 7):
        print(i)
    if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
        pass
    else:
        print(i)
