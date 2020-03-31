#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 @author: Haifeng Li
 @date: March 31, 2020
'''

from ncclient import manager
import requests

requests.packages.urllib3.disable_warnings()

host = '10.106.53.53'
user = 'admin'
password = 'Cisco123'
set_ip_address = '100.100.100.102'
set_subnet_mask = '255.255.255.0'
url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/address/primary".format(
    h=host)
payload = {}
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

with manager.connect(
        host=host, port=830, username=user,
        password=password, device_params={'name': 'iosxr'},
        hostkey_verify=False) as m:

    response_before = requests.request(
        "GET",
        url,
        auth=(
            user,
            password),
        data=payload,
        headers=headers,
        verify=False)
    if response_before.text:
        ip_before = response_before.json(
        )['Cisco-IOS-XE-native:primary']['address']
        mask_before = response_before.json(
        )['Cisco-IOS-XE-native:primary']['mask']

        with open("remove-ietf-interfaces.xml", 'r') as f2:
            remove_interface = f2.read().format(
                int_name='GigabitEthernet2',
                int_desc='remove ip address',
                ip_address=ip_before,
                subnet_mask=mask_before
            )

            set_remove_interface = m.edit_config(
                target="running", config=remove_interface)

    with open("config-ietf-interfaces.xml", 'r') as f3:
        set_interface = f3.read().format(
            int_name='GigabitEthernet2',
            int_desc='set ip address',
            ip_address=set_ip_address,
            subnet_mask=set_subnet_mask
        )

        set_config_interface = m.edit_config(
            target="running", config=set_interface)

        response_current = requests.request(
            "GET",
            url,
            auth=(
                user,
                password),
            data=payload,
            headers=headers,
            verify=False)

        ip_current = response_current.json(
        )['Cisco-IOS-XE-native:primary']['address']
        mask_current = response_current.json(
        )['Cisco-IOS-XE-native:primary']['mask']

if 'ip_before' in dir():
    print('IP address changed from [ {} {} ] to [ {} {} ].'.format(
        ip_before, mask_before, ip_current, mask_current))
else:
    print(
        'There is no IP address configured, IP address is configured as [ {} {} ].'.format(
            ip_current, mask_current))
