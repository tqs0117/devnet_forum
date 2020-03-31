#! /usr/bin/env python

from ncclient import manager

# Device Info
ios_xe1 = {
             "address": "10.124.41.193",
             "port": 830,
             "username": "cisco",
             "password": "cisco"
           }

# NETCONF Config Template to use
netconf_template = open("config-temp-ietf-interfaces.xml").read()

# Build the XML Configuration to Send
netconf_payload = netconf_template.format(int_name="GigabitEthernet2",
                                          int_desc="Configured by NETCONF",
                                          ip_address="10.255.255.1",
                                          subnet_mask="255.255.255.0"
                                          )
print("Configuration Payload:")
print("----------------------")
print(netconf_payload)

with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                     username=ios_xe1["username"],
                     password=ios_xe1["password"],
                     hostkey_verify=False) as m:
    # Send NETCONF <edit-config>
    netconf_reply = m.edit_config(netconf_payload, target="running")

    # Print the NETCONF Reply
    print(netconf_reply)
