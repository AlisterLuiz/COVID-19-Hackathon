from django.shortcuts import render
import pyrebase
from googleplaces import GooglePlaces, types, lang
import random

config = {
    "apiKey": "AIzaSyBk3hKgOO2SrqosNhsmipgEzi_tHQ921lE",
    "authDomain": "covid-19-85e6d.firebaseapp.com",
    "databaseURL": "https://covid-19-85e6d.firebaseio.com",
    "storageBucket": "covid-19-85e6d.appspot.com",
    "serviceAccount": "Server\COVID19_Hackathon\essentials_app\covid.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


# Create your views here.

def hi(request):
    return render(request, 'essentials_app/hi.html')


def insertData(request):
    lana = {"name": "Lana Kane", "agency": "Figgis Agency"}
    db.child("agents").child("Lana").set(lana)
    archer = {"name": "Sterling Archer", "agency": "Figgis Agency"}
    db.child("agents").push(archer)
    return render(request, 'essentials_app/hi.html')


google_places = GooglePlaces("AIzaSyDb5kEEULH5xs30Beq-dsKnQqbsdjX6AKI")

query_result = google_places.nearby_search(
    lat_lng={'lat': 25.2048, 'lng': 55.2708},
    radius=50000,
    types=[types.TYPE_GROCERY_OR_SUPERMARKET])

x = 0

places = []

for place in query_result.raw_response["results"]:
    x = x+1
    if x % 4 == 0:
        obj = dict()
        obj["id"] = place["id"]
        obj["location"] = place["geometry"]["location"]
        obj["name"] = place["name"]
        obj["vicinity"] = place["vicinity"]
        obj["openTill"] = random.choice(
            ["08:00", "09:00", "10:00", "11:00", "00:00", "01:00"])
        obj["occupancy"] = random.randint(3, 15)
        obj["pickup"] = random.choice([True, False])
        obj["homeDelivery"] = random.choice([True, False])
        obj["type"] = "SUPERMARKET"
        places.append(obj)


for place in places:
    print("========================")
    print(place)
