#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 @author: Haifeng Li
 @date: April 13, 2020
'''

import cli

config_interface = cli.configurep(
    ["interface GigabitEthernet3", "ip add 1.1.1.1 255.255.255.0", "no shutdown", "end"])

print(config_interface)
