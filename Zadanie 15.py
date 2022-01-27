import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

timeBefore = timedelta(days=7)
searchDate = datetime.today() - timeBefore

print(int(searchDate.timestamp()))

params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : "int(searchDate.timestamp())",
    "tagged" : "python",
    "min" : "15"  }

r = requests.get("https://api.stackexchange.com/2.2/questions/", params)
"""
try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format pliku")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
"""