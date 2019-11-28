import requests as req
import json

response = req.post('http://ada.marlboroughcollege.org/api/v1/public/home/almanac', data = None, json = disctionaryObject)
print(response.status_code)
print(response.text)
print(response.json())


