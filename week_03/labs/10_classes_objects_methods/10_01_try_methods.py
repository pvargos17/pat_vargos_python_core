'''
Read the documentation of the string methods at:
http://docs.python.org/3/library/stdtypes.html#string-methods.
You might want to experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate
optional arguments. So sub is required, but start is optional, and if
you include start, then end is optional.

Demonstrate below:
- strip



- replace


- find



Source: Exercise in chapter "Strings" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2009.html

'''


#- strip
def human_resource(hr):
    return hr.strip('Tosn')
x = "Tobby Flenderson"
print(human_resource(x))

#- replace

def accounting(a):
    return a.replace("White","Schrute")
x = "Angela White"
print(accounting(x))

# find
def unknown_job(c):
    return c.find('r',3,7)
x = "Creed Branson"
print(unknown_job(x))



# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found
#  within the slice s[start:end]. Optional arguments start and
#  end are interpreted as in slice notation. Return -1 if sub is not found.


