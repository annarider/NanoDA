import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.

    data = requests.get(url).text
    data = json.loads(data)

    json.dumps(data['topartists']['artist'][0], indent=4, sort_keys=True)

    for artist in data['topartists']['artist']:
        if artist['@attr']['rank'] == '1':
            return artist['name']

    
    return "not found"

print api_get_request('http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=0302e47a1eb053e8028f63c469350b26&format=json')
