# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict

# open the data file and load the JSON
with open("./30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

eCounter = defaultdict(int)

# TODO: Count the elements in the list
for q in data["features"]:
   eCounter[q['properties']['type']] += 1
   
print(eCounter)
