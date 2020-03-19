#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 @author: Haifeng Li
 @date: March 19, 2020
'''
import json
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Name', 'Product', 'Time']

with open('namelist_all.json', 'rb') as f:
    data = json.load(f)['DevNet_Forum_Participants']
    for data_person in data:
        name = data_person['name']
        for data_product in data_person['product']:
            table.add_row([name, data_product['name'], data_product['years']])

print(table)
