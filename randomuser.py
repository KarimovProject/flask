import json
import requests
import pprint

def main():
    
    url = 'https://randomuser.me/api'
    
    r = requests.get(url)
    
    base = r.json()
    results = base['results'][0]
    data = {
        "first_name" : results['name']['first'],
        "last_name" : results['name']['last'],
        
    }
    return data

pprint.pprint(main())