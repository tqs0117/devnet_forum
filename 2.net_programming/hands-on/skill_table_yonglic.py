#!/usr/bin/env python3
  
'''
  @author: Yongli Chen
  @date: April4, 2020
'''

import json
from tabulate import tabulate

table_header = ['Name','Product','Time']
table_data = []

with open('namelist_all.json') as f:
    file = json.load(f)["DevNet_Forum_Participants"]
    for file_person in file:
        name = file_person['name']
        for file_product in file_person['product']:
            table_data.append((name,file_product['name'],file_product['years']))

print(tabulate(table_data, headers=table_header))
