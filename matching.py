import json
import datetime
import random

def open_file():
    with open("users_data_fornat.json", "r", encoding="utf-8") as file:
        datas = json.load(file)
    return datas

data = open_file()
current_time = datetime.datetime.now()

def custom_date(user):
    user_date = datetime.datetime.strptime(user["date"], "%Y-%m-%d %H:%M:%S")
    return (user_date < current_time, user_date)

sort_data = sorted(data["users"], key=custom_date)

last_print_answer = {}

def matching_user(locate):
    sublocation = {}

    for user in sort_data:
        if not user["status"]:
            location = user["location"]
            splocate = location.split("-")
            result = splocate[1] if len(splocate) > 1 else splocate[0]
            if result in sublocation:
                sublocation[result].append({
                    "id": user["id"],
                    "name": user["name"],
                    "location": result
                })
            else:
                sublocation[result] = [{
                    "id": user["id"],
                    "name": user["name"],
                    "location": result
                }]
    if locate in sublocation:
        print(locate)
        del sublocation[locate]      
        print(sublocation)


# Example usage:
matching_user("โลตัส")


