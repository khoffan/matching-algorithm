import random
import json
import uuid
import datetime
import time


user_data = {"users":[]}
count = 1
num = 1
current_date = datetime.datetime.now()
while count < 11:
    username = random.choice(["john", "may", "king", "max"])
    location = random.choice(["USA", "Maxcio", "Canada", "England", "Thailand", "Agentina", "Korea", "japan"])
    status = random.choice([True,False])
    # timeDate = datetime.datetime.now()
    current_date -= datetime.timedelta(days=1)
    current_dates = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # print(current_date)
    
    ids = str(uuid.uuid4())
    count += 1
    user_data["users"].append({
        "id": ids,
        "name": username,
        "status": status,
        "locate":{
            "location": location,
        },
        "date": current_dates,
    })

# print(user_data)
with open("users_data_fornat.json", "w") as file_json:
    json.dump(user_data, file_json, indent=2)

print("user save data success")