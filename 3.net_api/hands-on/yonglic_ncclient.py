#!/usr/bin/env python3

'''
  @author: Yongli Chen
  @date: April4, 2020
'''

from ncclient import manager

csr1000v = {
             "hostip": "10.124.41.199",
             "port": 830,
             "username": "admin",
             "password": "Cisco123"
            }

netconf_template = open("config-temp-ietf-interfaces.xml").read()

netconf_payload = netconf_template.format(int_name='GigabitEthernet2',
                                          int_desc='Configured by NETCONF',
                                          ip_address='100.1.1.1',
                                          subnet_mask='255.255.255.0'
                                          )

print(netconf_payload)

with manager.connect(host=csr1000v["hostip"], port=csr1000v["port"], 
                     username=csr1000v["username"],
                     password=csr1000v["password"],
                     hostkey_verify=False) as m:

      netconf_reply = m.edit_config(netconf_payload, target="running")

      print(netconf_reply)
