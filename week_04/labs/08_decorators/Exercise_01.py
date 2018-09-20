'''
Write a decorator function that wraps text passed to it in <p> tags.

'''
def lowercase(func):
    def wrap(text):
        first_result = func(text)
        new_result = first_result.lower()
        return f"<p>{new_result}<p>"
    return wrap

@lowercase
def say_something(text):
    return text

print(say_something("Hey, you!"))


# def p_decorate(func):
