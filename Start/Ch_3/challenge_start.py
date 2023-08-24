# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("./30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def mostSignificantQuakes(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig


significantevents = sorted(
    data["features"], key=mostSignificantQuakes, reverse=True)
significantevents = significantevents[:40]
significantevents.sort(key=lambda e: e["properties"]["time"], reverse=True)
# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
header = ["Magnititude", "Place", "Felt Reports", "Date", "Link"]
rows = []
# TODO: populate the rows with the resulting quake data
for quake in significantevents:
    thedate = datetime.date.fromtimestamp(
        int(quake["properties"]["time"]/1000))
    lat = quake["geometry"]["coordinates"][1]
    long = quake["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com/maps/search/?api=1query={lat}%2C{long}"

    rows.append(
        [quake["properties"]["mag"],
         quake["properties"]["place"],
         0 if quake["properties"]["felt"] is None else quake["properties"]["felt"],
         thedate,
         gmaplink
         ]
    )

# TODO: write the results to the CSV file

with open("significantevents.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
