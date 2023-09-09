import json
import datetime


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

def matching_user(locate):
    user_locate = {}
    
    for data in sort_data:
        if(data["status"] == False):
           locates =data["locate"]["location"]
           if(locate == locates):
                user_locate.setdefault(locates, []).append(data["name"])
    
    if locate in user_locate:
        for name in user_locate[locate]:
            print(name)

matching_user("Canada")