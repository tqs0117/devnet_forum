import sys
import json

json_file = str(sys.argv[1])
namelist = open(json_file).read()
json_data = json.loads(namelist)

i = 0

while i < len(json_data["DevNet_Forum_Participants"][0]["language"]):
    print(json_data["DevNet_Forum_Participants"][0]["language"][i]["name"])
    i = i + 1