from django.shortcuts import render
import pyrebase
from googleplaces import GooglePlaces, types, lang
import random
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
import geocoder
import json
from django.conf import settings
import os

def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote

g = geocoder.ip('me')
lat = g.latlng[0]
lng = g.latlng[1]

config = {
  "apiKey": "AIzaSyBk3hKgOO2SrqosNhsmipgEzi_tHQ921lE",
  "authDomain": "covid-19-85e6d.firebaseapp.com",
  "databaseURL": "https://covid-19-85e6d.firebaseio.com",
  "storageBucket": "covid-19-85e6d.appspot.com",
  "serviceAccount": os.path.join(settings.BASE_DIR, "essentials_app/covid.json")
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'shops/browse.html', {'message':'this is a lol'})

class AboutPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'shops/browse.html', context=None)
        
    def post(self, request, **kwargs):
        print("POST ROUTE CALLED!")
        print(request.POST["radius"])
        print(self)
        data = matchData(request)
        return render(request, 'shops/browse.html', {'list' : data}) 
        

def matchData(request):
    google_places = GooglePlaces("AIzaSyDb5kEEULH5xs30Beq-dsKnQqbsdjX6AKI")

    if (request.POST["type"] == "SUPERMARKET"):
        t = [types.TYPE_GROCERY_OR_SUPERMARKET]
    else:
        t = [types.TYPE_PHARMACY]

    query_result = google_places.nearby_search(
            lat_lng = {'lat': lat, 'lng': lng}, 
            radius = int(request.POST["radius"]),
            types = t ) 

    checkResult = query_result.raw_response["results"]
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(checkResult)

    db_results = db.child("entities").get().val()

    dt = dict(db_results)
    lt = list(dt.values())
    result = filter(lambda x: x["type"] == request.POST["type"], lt) 
    result = list(result)

    newList = []

    print(result[0]["id"])
    print("======================")
    print(checkResult[0]["id"])
    print("======================")

    for r1 in result:
        for r2 in checkResult:
            if(r1["id"] == r2["id"]):
                newList.append(r1)
                break
    
    print("#######################")
    print(newList)

    return newList

            
     


def insertData(request):

    google_places = GooglePlaces("AIzaSyDb5kEEULH5xs30Beq-dsKnQqbsdjX6AKI")

    query_result = google_places.nearby_search(
            lat_lng={'lat': 25.3374, 'lng': 55.4121}, 
            radius=2000,
            types=[types.TYPE_GROCERY_OR_SUPERMARKET])

    x=0

    places = []

    for place in query_result.raw_response["results"]:
        x=x+1
        print(x)
        print("*****")
        if x%2==0:
            obj = dict()
            obj["id"] = place["id"]
            obj["location"] = str(place["geometry"]["location"])
            obj["name"] = place["name"]
            obj["vicinity"] = place["vicinity"]
            obj["openTill"] = random.choice(["08:00", "09:00", "10:00", "11:00", "00:00", "01:00"])
            obj["occupancy"] = random.randint(3,15)
            obj["pickup"] = random.choice([True, False])
            obj["homeDelivery"] = random.choice([True, False])
            obj["type"] = "SUPERMARKET"
            places.append(obj)
            

    for place in places:
        print("========================")
        print(place)
        db.child("entities").push(place)

    return true 
   
        