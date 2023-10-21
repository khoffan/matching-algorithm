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

customer_user = []

def customer_users():
    for user in sort_data:
        if user['status'] == False:
            customer_user.append({user['id'], user['name']})
    return customer_user
def matching_user(Locate):
    last_print_answer = []
    for user in data['users']:
        if user['status'] == True:
            if Locate == "รับงานทั้งหมด":
                if user['location'] == "รับงานทั้งหมด":
                    # print(user['name'])
                    last_print_answer.append(user['name']) == user['id']
                # else:
                #     print(user['name'])
                #     last_print_answer.append(user['name']) == user['id']
            elif Locate != "รับงานทั้งหมด":
                if user['location'] == Locate:
                    # print(user['name'])
                    last_print_answer.append(user['name']) == user['id']
                # else:
                #     print(user['name'])
                #     last_print_answer.append(user['name']) == user['id']
    for lastuser in last_print_answer:
        if lastuser in last_print_answer:
            print(lastuser)
            last_print_answer.remove(lastuser)
        else:
            print("ไม่มีข้อความนี้อยู่")
        
# Example usage:
print(customer_users())
# matching_user("รับงานทั้งหมด")
# matching_user("หอพัก-โลตัส")
# matching_user("หอพัก-โรงช้าง")


