import requests
response = requests.get('http://api.open-notify.org/astros.json', timeout=2.5)

json = response.json()
for person in json['people']:
    print(person['name'])
    