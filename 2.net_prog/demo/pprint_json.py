import sys
import json
from pprint import pprint

json_file = str(sys.argv[1])
namelist = open(json_file).read()

json_data = json.loads(namelist)

print("===== Output by print() =====")
print(json_data)
print("")
print("===== Output by pprint() =====")
pprint(json_data)
