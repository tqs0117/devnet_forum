import requests

url = "https://api.icndb.com/jokes/random"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))