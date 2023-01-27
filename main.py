from bs4 import BeautifulSoup
import requests
import logging
import os
from dotenv import load_dotenv
# from apscheduler.schedulers.blocking import BlockingScheduler
import time

import pyrebase

# load_dotenv()

FIREBASE_CONFIG = {
  "apiKey": "AIzaSyDg8-HLK6LmbChoGyLbN5Sga1NwjjzFMKA",
  "authDomain": "wspin-liga-stats.firebaseapp.com",
  "databaseURL":"gs://wspin-liga-stats.appspot.com",
  "projectId": "wspin-liga-stats",
  "storageBucket": "wspin-liga-stats.appspot.com",
  "messagingSenderId": "689090440669",
  "appId": "1:689090440669:web:c5f9095f58848338bbda34",
  "measurementId": "G-87J86NVY12"
}
def configure_firebase() -> dict[str, str]:
    
    load_dotenv()
    firebase_config = {
        "apiKey": os.getenv('apiKey'),
        "authDomain": os.getenv('authDomain'),
        "databaseURL":os.getenv('databaseURL'),
        "projectId": os.getenv('projectId'),
        "storageBucket": os.getenv('storageBucket'),
        "messagingSenderId": os.getenv('messagingSenderId'),
        "appId": os.getenv('appId'),
        "measurementId": os.getenv('measurementId')
    }
    return firebase_config

def get_parsed_page_html_code(path: str):

    html_doc = requests.get(path)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    return soup

def put_file_to_firebase(config: dict[str, str], path_on_cloud: str, path_local: str) -> None:
    firebase = pyrebase.initialize_app(config)

    storage = firebase.storage()

    storage.child(path_on_cloud).put(path_local)
    
def some_job(config) -> None:
    
    # get html_code
    html_code = get_parsed_page_html_code('https://liga.blokline.pl/Results/Index/8')
    
    # save html_code locally with name based on current datetime
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file_name = f"data/{timestr}.html"
    with open(file_name, mode="w") as f:
        f.write(str(html_code))
    
    # send html_code to firebase
    put_file_to_firebase(config, 
                         path_on_cloud=file_name,
                         path_local=file_name)
def download_files(filenames: list, config: dict[str, str]):
    firebase = pyrebase.initialize_app(config)

    storage = firebase.storage()

    for filename in filenames:
        data = storage.child(f"data/{filename}").download(filename = f"data/html/{filename}", path=f"data/{filename}")

if __name__ == '__main__':
    
    firebase_config = FIREBASE_CONFIG
    
    # scheduler = BlockingScheduler()
    # scheduler.add_job(some_job, 'interval', minutes = 5)
    # scheduler.start()
    
    # # do job once a 5 minutes
    # some_job(config = firebase_config)

    

    filenames = [
        "20230104-143204.html",
        "20230105-143203.html",
        "20230106-143205.html",
        "20230107-143203.html",
        "20230108-143204.html",
        "20230109-143203.html",
        "20230110-143204.html",
        "20230111-143203.html",
        "20230112-144203.html",
        "20230113-143205.html",
        "20230114-143206.html",
        "20230115-143203.html",
        "20230116-143203.html",
        "20230117-143203.html",
        "20230118-143205.html",
        "20230119-143206.html",
        "20230120-143203.html",
        "20230121-143206.html",
        "20230122-143204.html",
        "20230123-143206.html",
        "20230124-143203.html",
        "20230125-143204.html",
        "20230126-143203.html",
        # 27
        # 28
    ]
    download_files(filenames, firebase_config)
    


    