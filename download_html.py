import pyrebase
from dotenv import load_dotenv

from scrapper import configure_firebase

FILENAMES = [
        # "20230104-143204.html",
        # "20230105-143203.html",
        # "20230106-143205.html",
        # "20230107-143203.html",
        # "20230108-143204.html",
        # "20230109-143203.html",
        # "20230110-143204.html",
        # "20230111-143203.html",
        # "20230112-144203.html",
        # "20230113-143205.html",
        # "20230114-143206.html",
        # "20230115-143203.html",
        # "20230116-143203.html",
        # "20230117-143203.html",
        # "20230118-143205.html",
        # "20230119-143206.html",
        # "20230120-143203.html",
        # "20230121-143206.html",
        # "20230122-143204.html",
        # "20230123-143206.html",
        # "20230124-143203.html",
        # "20230125-143204.html",
        # "20230126-143203.html",
        "20230127-143204.html",
        "20230128-143203.html"
    ]

def download_files(filenames: list, config: dict[str, str]):
    firebase = pyrebase.initialize_app(config)

    storage = firebase.storage()

    for filename in filenames:
        data = storage.child(f"data/{filename}").download(filename = f"data/html/{filename}", path=f"data/{filename}")

if __name__ == '__main__':
    
    firebase_config = configure_firebase()

    download_files(FILENAMES, firebase_config)