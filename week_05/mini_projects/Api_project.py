from pprint import pprint
import requests

c = requests.get("http://ip-api.com/json",json=True)

data = c.json()
pprint(data)
city = data['city'] # this is grabbing the city name from the city key in the dict
print(city)

r = requests.get(f"http://beermapping.com/webservice/locquery/44a8826612022c756825a7205f0b52a2/{city}&s=json",
                    json=True)
            # importing the city name into this url that will direct you to that citys given brewery

brewerys = r.json()

pprint(brewerys) # printing the list of given brewerys in that city.


