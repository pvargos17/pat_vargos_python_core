'''
Write the necessary code that prints out the area and circumference
of a circle with a radius of 3.14

'''
radius = 3.14
pi = 4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11))
area = pi * radius**2
circumference = 2*pi*radius

print(area)
print(circumference)
