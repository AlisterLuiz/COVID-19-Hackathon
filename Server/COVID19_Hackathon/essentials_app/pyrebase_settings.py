import pyrebase
config = {
  "apiKey": "AIzaSyBk3hKgOO2SrqosNhsmipgEzi_tHQ921lE",
  "authDomain": "covid-19-85e6d.firebaseapp.com",
  "databaseURL": "https://Covid-19.firebaseio.com",
  "storageBucket": "covid-19-85e6d.appspot.com",
  "serviceAccount": "./covid.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

