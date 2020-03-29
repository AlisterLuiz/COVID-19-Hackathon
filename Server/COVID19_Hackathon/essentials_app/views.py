from django.shortcuts import render
import pyrebase
from googleplaces import GooglePlaces, types, lang
import random
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.conf import settings
import os

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
        return render(request, 'hi.html', context=None)
    def post(self, request, **kwargs):
        print("POST ROUTE CALLED!")
        print(request.POST["username"])
        print(self)
        return render(request, 'hi.html', context=None)

# Create your views here.

# class SignUpView(CreateView):
#     template_name = 'essentials_app/low.html'
#     form_class = UserCreationForm

# def hi(request):
#     return render(request, 'essentials_app/hi.html')


def matchData(request):
    google_places = GooglePlaces("AIzaSyDb5kEEULH5xs30Beq-dsKnQqbsdjX6AKI")

    query_result = google_places.nearby_search(
            lat_lng={'lat': 25.3526878, 'lng': 55.3836953}, 
            radius=2000,
            types=[types.TYPE_GROCERY_OR_SUPERMARKET])


def insertData(request):

    google_places = GooglePlaces("AIzaSyDb5kEEULH5xs30Beq-dsKnQqbsdjX6AKI")

    query_result = google_places.nearby_search(
            lat_lng={'lat': 25.3526878, 'lng': 55.3836953}, 
            radius=2000,
            types=[types.TYPE_GROCERY_OR_SUPERMARKET])

    x=0

    places = []

    for place in query_result.raw_response["results"]:
        x=x+1
        print(x)
        print("*****")
        if x%1==0:
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

    return render(request, 'essentials_app/hi.html')    
   
        