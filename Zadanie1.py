# def moj_tekst():
#    print("Cześć to ja Twoja funkcja")
# moj_tekst()

# def pozdrowienia():
#    print("Pozdrowienie od moje funkcji!")
# pozdrowienia()

# def dodawanie():
#    return 2 + 5
#    print("Wynik dodawania wynosi:" , dodawanie())
# dodawanie()


# def data_twoich_urodzin():
#    twoje_imie = "Remek"
#    data = 1981
#    print("Witaj", twoje_imie, "rok Twojego urodzenia to", data)
# data_twoich_urodzin()

# def ile_lat_w_2050():
#    data = 1981
#    rok_2050 = 2050
#    wynik = rok_2050 - data
#    print ("W roku 2050 będziesz miał", wynik, "lat :)")
# ile_lat_w_2050()

def user_ile_lat_w_2050():
    print("Podaj rok urodzenia")
    wiek_user_data = input()
    rok_2050 = 2050
    wynik = rok_2050 - int(wiek_user_data)
    print("W roku 2050 będziesz miał", wynik, "lat :)")
user_ile_lat_w_2050()