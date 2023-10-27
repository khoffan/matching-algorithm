from sortDatas import SortDatas

datasort = SortDatas()

sort_data = datasort.sort_data()

customer_user = []
def sort_ids():
    for user in sort_data:
        customer_user.append({"id":user["id"],"name": user['name'], "location": user["location"]})
    return customer_user

