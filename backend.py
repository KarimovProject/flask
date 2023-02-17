import requests
import pprint
import json

r = requests.get('https://randomuser.me/api/')

data = r.json()

result = data['results'][0]
age = result['id']['value']
pprint.pprint(age)