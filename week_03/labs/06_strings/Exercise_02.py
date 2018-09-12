'''
Complete Exercise 8.3 (p.79) from the textbook.

'''
def is_palindrome(s):
    b = s.lower()
    if b == b[::-1]:
        return True
    return False

print(is_palindrome("car"))
