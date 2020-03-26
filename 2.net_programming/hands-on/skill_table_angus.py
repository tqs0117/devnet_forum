import json
from tabulate import tabulate


namelist = open("./namelist_all.json", encoding='utf-8')
handbook = json.load(namelist)["DevNet_Forum_Participants"]

table_header = ["Name", "Product", "Time"]
table_data = []


for person in handbook:
    person_name = person['name']
    for product in person["product"]:
        table_data.append((person_name, product['name'], product['years']))


print(tabulate(table_data, headers=table_header, tablefmt='grid'))