import sys
import json
from tabulate import tabulate

json_file = str(sys.argv[1])
namelist = open(json_file).read()
json_data = json.loads(namelist)

table_header = ["Name", "Product", "Time"]
table_data = []

for participant in json_data["DevNet_Forum_Participants"]:
    name = participant["name"]
    for product in participant["product"]:
        product_name = product["name"]
        product_age = product["years"]
        table_data.append((name, product_name, product_age))

print(tabulate(table_data, headers=table_header))