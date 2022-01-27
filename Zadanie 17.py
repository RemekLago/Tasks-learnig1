import requests
import json
import pprint
import webbrowser



def take_url_of_cat_breed(chosen_pet):
    params = {
        "amount": 1,
        "id": str(chosen_pet)
       }

    r = requests.get("https://api.thecatapi.com/v1/breeds", params)

    try:
        content_site = r.json()
    except json.decoder.JSONDecodeError:
        print("The format of file is incorrect")
    else:
        for cat in content_site:
            print(cat["url"])

def breed_cat(chosen_breed):
    chosen_pet = 0
    if (chosen_breed == 1):
        chosen_pet = "beng"
    elif (chosen_breed == 2):
        chosen_pet == "birm"
    elif (chosen_breed == 3):
        chosen_pet == "buri"
    elif (chosen_breed == 4):
        chosen_pet == "aege"
    else:
        Print("Something went wrong")
    return chosen_pet

print("""Please choose cat breed that you want to see.
    1. Bengal 
    2. Birman 
    3. Burmilla
    4. Aegean
    """)
chosen_breed = int(input("What breed of cat you want to see: "))
breed_cat(chosen_pet)
print(chosen_pet)
#take_url_of_cat_breed(chosen_pet_name)