import os
from dotenv import load_dotenv
import json

# from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime, timezone
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

<<<<<<< HEAD
path = os.getenv("SERVICES_ACCOUT_FILE")
=======


path = os.getenv('SERVICE_FIREBASE')
>>>>>>> d0af984f589d99fd729102e1470d2a906e44d927
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
    data = doc.to_dict()

    documentId = doc.id
    # print(f"usersts : {statususer} and role : {role}")
    if data["name"] != "" and data["stdid"] != "":
        name = data["name"]
        locate = data["locattion"]
<<<<<<< HEAD
        statususer = data["status"]
        role = data["role"]
        working = data["statuswork"]
=======
        status = data["role"]
        statususer = data["status"]
>>>>>>> d0af984f589d99fd729102e1470d2a906e44d927
        datenano = data["date"]
        date = timeformate(datenano)
        all_users["users"].append(
            {
                "id": documentId,
                "name": name,
                "location": locate,
                "role": role,
                "statususer": statususer,
                "working": working,
                "date": date,
            }
        )
# print(all_users)
try:
    with open("../all_user_in_db.json", "w", encoding="utf-8") as file_json:
        json.dump(all_users, file_json, ensure_ascii=False, indent=2)
        print("save data success")
except Exception as e:
    print(f"e = {e}")
