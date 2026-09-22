#100 Days of Code
#Author: Mathias Nerd
#Distionary in list (practicing nesting of dictionaries)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visits, cities):
    initial_dict = {}
    initial_dict["country"] =  country
    initial_dict["visits"] = visits
    initial_dict["cities"] = cities
    travel_log.append(initial_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)