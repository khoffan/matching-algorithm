import json
import datetime
import random

def open_file():
    with open("users_data_fornat.json", "r") as file:
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
    user_locate = {}
    
    # Get the last printed answer for this location, or initialize it to None
    last_answer = last_print_answer.get(locate, None)
    
    for user in sort_data:
        if not user["status"]:
            for content in user["content"]:
                if content["location"] == locate and user["name"] != last_answer:
                    user_locate.setdefault(locate, []).append(user["name"])
    
    if locate in user_locate:
        if user_locate[locate]:
            # Select a random answer from the available answers
            next_answer = random.choice(user_locate[locate])
            print(next_answer)
            last_print_answer[locate] = next_answer
        else:
            print("No data")

# Example usage:
matching_user("Canada")
matching_user("Thailand")
matching_user("Korea")
