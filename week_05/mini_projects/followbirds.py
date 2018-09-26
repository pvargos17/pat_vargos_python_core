'''
Using the tweepy package, build a script that classifies a twitter handle
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''


import tweepy
from pprint import pprint


auth = tweepy.OAuthHandler("GE8oeAmqFrMRL4OhvPtTKHfcg","5OzRsCepFYrAtu37UrVlkGeX2PUrDBHGGFwIXcRaGw4OINdlIk")
auth.set_access_token("1030462573555019776-mU2lHEsZhPBzwkFnsxxGqNLxy12C8P","OQBxKFirkD8Ecc7Y7yhbNR4QaHGHgI6tEyiTI8t6Eii5m")

api = tweepy.API(auth)

user_list = ['Croc_a_Dogs', 'ChookByTheBook', 'MPSquared_']

# user1 = api.get_user(user_list[0])
# user2 = api.get_user(user_list[1])
# user3 = api.get_user(user_list[2])
# count = user.followers_count
# #pprint(user)

def counter(l):
    list_1 = []
    list_2 = []
    list_3 = []
    for x in l:
        user = api.get_user(x)
        count = user.followers_count
        #print(x + " has " + count + " followers")
        if count > 200:
            list_1.append(x)
        elif count > 170:
            list_2.append(x)
        else:
            list_3.append(x)
    print(f"{list_1[0]} has more than 200 followers, {list_2[0]} has more than 100 followers, and {list_3[0]} is a loser.")


user_list = ['Croc_a_Dogs', 'ChookByTheBook', 'MPSquared_']
print(counter(user_list))
     #    handle = x
     #    if count < 200
     #     print(f("{handle} is popular"))
     # elif:











# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet)
