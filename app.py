import random
import json
import uuid
import datetime
import time


unique_usernames = ["John", "May", "King", "Max", "Jason", "Vincton", "Janasis", "Oasis", "Markuz", "Jenifer"]

user_data = {"users":[]}
count = 1
number = 1
current_date = datetime.datetime.now()
while count < 11:
    username = random.choice(unique_usernames)
    unique_usernames.remove(username)
    location = random.choice(["รับงานทั้งหมด","หอพัก-โลตัส", "หอพัก-โรงช้าง"])
    status = random.choice([True,False])
    time_difference_minutes = random.randint(10, 30)
    day_diff = random.randint(0,3)
    # timeDate = datetime.datetime.now()
    current_date -= datetime.timedelta(days=day_diff, minutes=time_difference_minutes)
    current_dates = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # print(current_date)

    ids = str(uuid.uuid4())
    count += 1
    user_data["users"].append({
        "id": ids,
        "name": username,
        "status": status,
        "location": location,
        "date": current_dates,
    })
        

# print(user_data)
with open("users_data_fornat.json", "w", encoding="utf-8") as file_json:
    json.dump(user_data, file_json, ensure_ascii=False, indent=2)
    print("user save data success")

