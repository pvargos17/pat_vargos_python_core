'''
Complete Exercise 8.2 (p.79) from the textbook.

'''
def a_counter(s,a):
    count = 0
    for letter in s:
        if letter == a:
            count += 1
    return count
print(a_counter("banana", "a"))
