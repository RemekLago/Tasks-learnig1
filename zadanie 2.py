
suma_liczb = 0
i = 0

while i < 3:
    x = int(input("Podaj liczbę: "))
    if (x > 0 and x % 2 == 0):
        suma_liczb += x
        i +=1
        print ("obecny wynik sumy to: ", suma_liczb)
    else:
        print("Podaj liczbę parzystą")
print("\nKońcowy wynik sumy to: ", suma_liczb)
