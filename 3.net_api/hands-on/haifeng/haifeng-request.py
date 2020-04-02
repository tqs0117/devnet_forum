#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 @author: Haifeng Li
 @date: March 31, 2020
'''

import requests

requests.packages.urllib3.disable_warnings()

host = '10.106.53.53'
user = 'admin'
password = 'Cisco123'

url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/address/primary".format(
    h=host)
payload = "{\"primary\": {\"address\": \"100.100.100.3\", \"mask\": \"255.255.255.0\"}}"

headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

response = requests.request("PATCH", url, auth=(user, password),
                            data=payload, headers=headers, verify=False)

response_current = requests.request(
    "GET",
    url,
    auth=(
        user,
        password),
    data=payload,
    headers=headers,
    verify=False)

ip_current = response_current.json()['Cisco-IOS-XE-native:primary']['address']
mask_current = response_current.json()['Cisco-IOS-XE-native:primary']['mask']

print('IP address changed to [ {} {} ].'.format(ip_current, mask_current))
