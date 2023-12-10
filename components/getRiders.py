from components.sortDatas import SortDatas

datasort = SortDatas()

sort_data = datasort.sort_data()

riders_user = []


def riders_sort():
    for user in sort_data:
        if user["role"] == True and user["statususer"] != "offline":
            riders_user.append(
                {
                    "id": user["id"],
                    "name": user["name"],
                    "location": user["location"],
                    "statususer": user["statususer"],
                    "date": user["date"],
                }
            )
    return riders_user


# print(riders_sort())
