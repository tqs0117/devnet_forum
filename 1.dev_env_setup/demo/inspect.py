#!/usr/bin/env python3

import sys
import json


json_file = str(sys.argv[1])

namelist = open(json_file).read()

json_data = json.loads(namelist)

team = json_data["DevNet_Forum_Participants"][0]["team"]
name = json_data["DevNet_Forum_Participants"][0]["name"]
location = json_data["DevNet_Forum_Participants"][0]["location"]
manager = json_data["DevNet_Forum_Participants"][0]["manager"]
blue_badge = json_data["DevNet_Forum_Participants"][0]["blue-badge"]
products = json_data["DevNet_Forum_Participants"][0]["product"]  # type: list
language = json_data["DevNet_Forum_Participants"][0]["language"]
hobbies = json_data["DevNet_Forum_Participants"][0]["hobbies"]

if blue_badge is True:
    os = "MacOS"
elif blue_badge is False:
    os = "Windows10"

print("\n")
# print("*******************************")
print("************自我介绍*************")
print("")

print("大家好, 我是来自%s Team的%s. 很高兴认识大家!" % (team, name))
print("")

print("我base在%s, 我的老板是%s." % (location, manager))
print("我在使用的操作系统是%s." % os)
print("")
# 产品
if len(products) > 1:
    for p in products:
        if p == products[-1]:
            print("以及%d年%s产品相关经验. " % (p["years"], p["name"]))
        elif p == products[0]:
            print("我有%d年%s产品相关经验, " % (p["years"], p["name"]), end="")
        else:
            print("%d年%s产品相关经验, " % (p["years"], p["name"]), end="")
else:
    for p in products:
        print("我有%d年%s产品相关经验. " % (p["years"], p["name"]))

# 语言
if len(language) > 1:
    for l in language:
        if l == language[-1]:
            print("以及%s水平的%s相关经验. " % (l["level"], l["name"]))
        elif l == language[0]:
            print("另外, 我有%s水平的%s相关经验, " % (l["level"], l["name"]), end="")
        else:
            print("%s水平的%s相关经验, " % (l["level"], l["name"]), end="")
elif len(language) == 1:
    for l in language:
        print("另外, 我有%s水平的%s相关经验. " % (l["level"], l["name"]))

elif len(language) == 0:
    print("我没有什么编程经验.. o(╯□╰)o")

print("")
print("我的兴趣爱好有" + hobbies)

print("")
