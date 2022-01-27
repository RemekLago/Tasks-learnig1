import requests
import json
import pprint
import webbrowser

params = {
    "amount": 5
   }

r = requests.get("http://cat-fact.herokuapp.com/facts/random", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format pliku")
else:
    for cat in content:
        print(cat["text"])