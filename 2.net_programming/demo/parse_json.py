import sys
import json
from pprint import pprint

json_file = str(sys.argv[1])
namelist = open(json_file).read()
json_data = json.loads(namelist)

team = json_data["DevNet_Forum_Participants"][0]["team"]
name = json_data["DevNet_Forum_Participants"][0]["name"]
location = json_data["DevNet_Forum_Participants"][0]["location"]
manager = json_data["DevNet_Forum_Participants"][0]["manager"]
blue_badge = json_data["DevNet_Forum_Participants"][0]["blue-badge"]
products = json_data["DevNet_Forum_Participants"][0]["product"]
language = json_data["DevNet_Forum_Participants"][0]["language"]
greetings = json_data["DevNet_Forum_Participants"][0]["greetings"]

print("===== Printing team =====")
pprint(team)
print("")

print("===== Printing name =====")
pprint(name)
print("")

print("===== Printing location =====")
pprint(location)
print("")

print("===== Printing manager =====")
pprint(manager)
print("")

print("===== Printing blue_badge =====")
pprint(blue_badge)
print("")

print("===== Printing products =====")
pprint(products)
print("")

print("===== Printing language =====")
pprint(language)
print("")

print("===== Printing greetings =====")
pprint(greetings)
print("")
