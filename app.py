import random
import json
import uuid
import datetime


user_data = {"users":[]}
count = 1

while count < 11:
    username = random.choice(["john", "may", "king", "max"])
    location = random.choice(["USA", "Maxcio", "Canada", "England", "Thailand", "Agentina", "Korea", "japan"])
    status = random.choice([True,False])
    time = datetime.datetime.now()
    format_time = time.strftime("%Y-%m-%d %H:%M:%S")
    ids = str(uuid.uuid4())
    user_data["users"].append({
        "id": ids,
        "name": username,
        "status": status,
        "locate":{
            "location": location,
        },
        "date": format_time,
    })
    count += 1

with open("users_data_fornat.json", "w") as file_json:
    json.dump(user_data, file_json, indent=2)

print("user save data success")