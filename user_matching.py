
# from components.getIds import sort_ids
from components.getCustomers import cusrtomer_sort
from components.getRiders import riders_sort

# ids = sort_ids()
customers = cusrtomer_sort()
riders = riders_sort()

def matching(customer, rider):
    matches = []

    for c in customer:
        for r in rider:
            if c['location'] == r['location']:
                matches.append({'customer_id': c['id'],'customer_name': c['name'], 'rider_id': r['id'],'rider_name': r['name']})

    return matches

matching_result = matching(customers,riders)
print(matching_result)


