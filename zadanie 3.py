print("Zgadnij liczbę w przedziale od 0 do 10, masz 4 próby")
szukana_liczba = 7
i = 0
# def Gra_w_zgadnij():
while i < 4:
    x = int(input("Podaj liczbę: "))
    if (x > szukana_liczba):
        print("Podana liczba ", x, "jest za duża")

    elif (x < szukana_liczba):
        print("Podana liczba ", x, "jest za mała")

    elif (x == szukana_liczba):
        print("Zgadłeś, szukana liczbą to: ", x)
        break
    i += 1
else:
    print("Niestety nie zgadłeś, zagraj jeszcze raz")
"""
y = input("Jeśli chcesz zagrać jeszcze raz wpisz T, jeśli chcesz zakończyć N: ")
if y == T:
    T = None
    N = None
    i == 0
elif y == N:
    print("Dziękuje za zabawę")
else:
    print("Jeśli chcesz zagrać jeszcze raz wpisz T, jeśli chcesz zakończyć N")
"""