'''
Improve the decorator from the previous exercise by allowing it to take
a tag as an input - making it more general.

'''
def tag_func(name)
    def lowercase(func):
        def wrap(text):
            first_result = func(text)
            new_result = first_result.lower()
            return f"<p>{new_result}<p>"
    return wrap

@tag_name("header")
def say_something(text):
    return f"Wrap in tags:{text}. Thanks!"

print(say_something("Hey, you!"))




# def tags(tag_name):
#     def tags_decorator(func):
#         def func_wrapper(name):
#             return f"<{tag_name}>{func(name)}</{tag_name}>"
#         return func_wrapper
#     return tags_decorator

# @tags("div")
# def get_text(text):
#     return f"Wrap me in tags: {text}. Thanks!"

# print(get_text("hei this part seems unwrapped!"))
