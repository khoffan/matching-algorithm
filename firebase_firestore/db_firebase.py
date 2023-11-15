import os
import subprocess
package_names = ["firebase-admin","python-dotenv"]
for package_name in package_names:
    subprocess.check_call(['pip', 'install', package_name])
from dotenv import load_dotenv
import json
# from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime, timezone
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

path = os.getenv('SERVICES_ACCOUT_FILE')
# Initialize Firebase with your service account key JSON file
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

# Reference to your collection
collection_ref = db.collection("deliverPost")

# Get all documents in the collection
docs = collection_ref.stream()

def timeformate(datenano):

    # Convert the string to a datetime object
    dt = datetime.strftime(datenano, "%Y-%m-%d %H:%M:%S")

    return dt

# Iterate over documents and print data
all_users = {"users": []}
count = 0
for doc in docs:
    count += 1
    data  = doc.to_dict()
    # print(data)
    documentId = doc.id
    if data["name"] != "":
        name = data["name"]
        locate = data["locattion"]
        status = data["satus"]
        datenano = data["date"]
        date = timeformate(datenano)
        all_users["users"].append({
            "id": documentId,
            "name": name,
            "location": locate,
            "role": bool(status),
            "date": date,
        })
# print(all_users)
try:
    with open("../user_in_db.json", "w", encoding="utf-8") as file_json:
        json.dump(all_users, file_json, ensure_ascii=False, indent=2)
        print("save data success")
except Exception as e:
    print(f"e = {e}")
