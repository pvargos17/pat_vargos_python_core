'''
Complete Exercise 3.2 (p.27) from the textbook.

'''

# def do_twice(func): #PART 1
#     func()
#     func()

# def print_spam():
#     print('spam')

# do_twice(print_spam)

# def do_twice(func,arg): #PART 2
#     func(arg)
#     func(arg)

# def print_spam():
#     print('spam')

# do_twice(print_spam, 'spam')

# def do_twice(func,arg): #PART 3
#     func(arg)
#     func(arg)

# def print_twice(arg):
#     print(arg)
#     print(arg)

# def print_spam():
#     print('spam')

# do_twice(print_spam)


# def do_twice(func,arg): #PART 4
#     func(arg)
#     func(arg)

# def print_twice(arg):
#     print(arg)
#     print(arg)

# def print_spam():
#     print('spam')

# do_twice(print_spam, 'spam')
# print('')



def do_twice(func,arg): #PART 5
    func(arg)
    func(arg)

def print_twice(arg):
    print(arg)
    print(arg)

def do_four(func, arg):
    do_twice(func,arg)
    do_twice(func,arg)

do_twice(print_twice, 'spam')
print('')

do_four(print_twice, 'spam')



