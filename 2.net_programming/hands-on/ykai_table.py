import json
import prettytable as pt

tb = pt.PrettyTable()
tb.field_names = ["Name", "Product", "Time"]

f = open('namelist_all.json',encoding='utf-8')
file = json.load(f)['DevNet_Forum_Participants']

for participant in file:
    name = participant["name"]
    for product in participant["product"]:
        tb.add_row([name,product["name"],product["years"]])
tb.set_style(pt.MSWORD_FRIENDLY)
print(tb)


