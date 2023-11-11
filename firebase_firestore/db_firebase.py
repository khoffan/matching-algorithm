import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

path = os.getenv("SERVICES_ACCOUT_FILE")
# Initialize Firebase with your service account key JSON file
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

# Reference to your collection
collection_ref = db.collection("userProfile")

# Get all documents in the collection
docs = collection_ref.stream()

# Iterate over documents and print data
for doc in docs:
    data  = doc.to_dict()

    documentId = doc.id
    name = data.get('name')
    lname = data.get('lname')
    stdid = data.get('stdid')
    print(f"name: {name} \t lname: {lname} \t stdid: {stdid}")
