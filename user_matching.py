
# from components.getIds import sort_ids
from components.getCustomers import cusrtomer_sort
from components.getRiders import riders_sort
import datetime

# ids = sort_ids()
customers = cusrtomer_sort()


def matching(customer):
    d_time = datetime.datetime.now()
    riders = riders_sort()
    matches = []
    rider_ids = set()
    customers_ids = set()
    for c in customer:
        for r in riders:
            if (
                r["id"] not in rider_ids
                and c["id"] not in customers_ids
                and (c["location"] == r["location"] or r["location"] == "รับทุกงาน")
            ):
                matches.append(
                    {
                        "customer_id": c["id"],
                        "customer_name": c["name"],
                        "rider_id": r["id"],
                        "rider_name": r["name"],
                        "date": d_time
                    }
                )
                rider_ids.add(r["id"])
                customers_ids.add(c["id"])
                break
    return matches


# matching_result = matching(customers)
# print(matching_result)

# riders = [riders for rider in riders if rider["id"] not in rider_ids]
