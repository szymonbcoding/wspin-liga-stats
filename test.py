import pyrebase

firebase_config = {
  "apiKey": "AIzaSyDg8-HLK6LmbChoGyLbN5Sga1NwjjzFMKA",
  "authDomain": "wspin-liga-stats.firebaseapp.com",
  "databaseURL":"gs://wspin-liga-stats.appspot.com",
  "projectId": "wspin-liga-stats",
  "storageBucket": "wspin-liga-stats.appspot.com",
  "messagingSenderId": "689090440669",
  "appId": "1:689090440669:web:c5f9095f58848338bbda34",
  "measurementId": "G-87J86NVY12"
}

firebase = pyrebase.initialize_app(firebase_config)

storage = firebase.storage()

path_on_cloud = "data/20230102-193703.html"
path_local = path_on_cloud
storage.child(path_on_cloud).put(path_local)