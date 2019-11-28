#To install from terminal type:
#sudo -H python3 -m pip install requests
import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("http://ada.marlboroughcollege.org/api/v1/public/home/almanac")

jprint(response.json())