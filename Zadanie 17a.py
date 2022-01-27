import requests
import json
import pprint
import webbrowser

print("""Please choose cat breed that you want to see.
    1. Bengal 
    2. Birman 
    3. Burmilla
    4. Aegean
    """)
chosen_pet = int(input("What breed of cat you want to see: "))

breed_id = {1: 'beng', 2: "birm", 3: "burm", 4: "aege"}

if (chosen_pet == 1):
    idFromUser = breed_id[1]
elif (chosen_pet == 2):
    idFromUser = breed_id[2]
elif (chosen_pet == 3):
    idFromUser = breed_id[3]
elif  (chosen_pet == 4):
    idFromUser = breed_id[4]
print(idFromUser)

params = {
    "amount": 1,
    "id": str("idFromUser")
       }

r = requests.get("https://api.thecatapi.com/v1/breeds", params)

try:
    content_site = r.json()
except json.decoder.JSONDecodeError:
    print("The format of file is incorrect")
else:
    for cat in content_site:
#        print(cat["wikipedia_url"])

pprint(content_site)