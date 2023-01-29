from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler
import time

import pyrebase


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

if __name__ == '__main__':
    
    firebase_config = configure_firebase()
    
    scheduler = BlockingScheduler()
    scheduler.add_job(some_job, 'interval', minutes = 5)
    scheduler.start()
    
    # do job once a 5 minutes
    some_job(config = firebase_config)

    
    


    