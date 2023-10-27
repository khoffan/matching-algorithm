import json
import datetime

class SortDatas:
    def __init__(self):
        with open("users_data_fornat.json", "r", encoding="utf-8") as file:
            datas = json.load(file)

        self.data = datas
        self.current_time = datetime.datetime.now()

    def custom_date(self, user):
        user_date = datetime.datetime.strptime(user["date"], "%Y-%m-%d %H:%M:%S")
        return (user_date < self.current_time, user_date)

    def sort_data(self):
        return sorted(self.data["users"], key=self.custom_date)
