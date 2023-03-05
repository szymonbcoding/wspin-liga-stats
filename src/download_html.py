import pyrebase

def download_files_from_firebase(filenames: list, config: dict[str, str]):
    firebase = pyrebase.initialize_app(config)

    storage = firebase.storage()

    for filename in filenames:
        data = storage.child(f"data/{filename}").download(filename = f"data/html/{filename}", path=f"data/{filename}")
