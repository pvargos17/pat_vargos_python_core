'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

# 86400 seconds in a day * 365 =

x = (86400*365)/6   #stat 1
y = (86400*365)/12  #stat 2
z = (86400*365)/40  #stat 3
pop1 = 380123456 + x - y + z
pop2 = pop1 + x + y - z
pop3 = pop2 + x + y - z

print(pop1)
print(pop2)
print(pop3)

