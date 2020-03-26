import requests

url = "https://10.124.41.193:443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("GET", url, headers=headers, data = payload, verify = False)

print(response.text.encode('utf8'))
