from components.sortDatas import SortDatas

datasort = SortDatas()

sort_data = datasort.sort_data()

customer_user =  []
def cusrtomer_sort():
    for user in sort_data:
        if user["role"] == False:
            customer_user.append({"id":user["id"],"name": user['name'], "location": user["location"], "date": user["date"]})
    return customer_user

# print(cusrtomer_sort())

