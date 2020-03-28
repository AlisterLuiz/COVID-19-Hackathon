from django.shortcuts import render
import pyrebase
config = {
  "apiKey": "AIzaSyBk3hKgOO2SrqosNhsmipgEzi_tHQ921lE",
  "authDomain": "covid-19-85e6d.firebaseapp.com",
  "databaseURL": "https://covid-19-85e6d.firebaseio.com",
  "storageBucket": "covid-19-85e6d.appspot.com",
  "serviceAccount": "D:/University/covid-19/COVID-19_Hackathon/Server/COVID19_Hackathon/essentials_app/covid.json"
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
    