#! /usr/bin/env python

from cli import configurep
import argparse

# Retrieve the interface from command line using argparse
parser = argparse.ArgumentParser()
parser.add_argument("interface", help="Interface to bring up")
args = parser.parse_args()

# List of commands to run
commands = [
            "interface {}".format(args.interface),
            "no shut"
           ]

# Run commands using Python API
# Commands need to be semicolon seperated
configurep(commands)