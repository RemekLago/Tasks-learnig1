uczniowie = {
    "12345": {"name": "Janek", "age": "27", "wieght": "80"},
    "23455": {"name": "Olek", "age": "23", "wieght": "90"},
    "34567": {"name": "Andrzej", "age": "26", "wieght": "100"},
    "74839": {"name": "Marek", "age": "30", "wieght": "55"},
    "93875": {"name": "Piotr", "age": "45", "wieght": "65"},
    "73654": {"name": "Adam", "age": "67", "wieght": "77"},
    "01818": {"name": "Tomek", "age": "44", "wieght": "89"},
    "37649": {"name": "Janek", "age": "55", "wieght": "55"},
            }

for id, dane in uczniowie.items():
    print("ID:", id) # podaje ID, czyli pierwszą kolumnę jako klucz
    print("Dane: ", dane) # podaje Dane, czyli listę przypożądkowaną do klucza ID
    for key in dane: 
        print(key, ":", dane[key])