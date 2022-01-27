import random
import time

user = 0
computer = 0

while True:
    print("proszę wpisz o lub r")
    x = input()
    if x == "0": break
    elif x == 'o' : x = "orzeł"
    elif x == 'r' : x = "reszka"
    else:
        print("proszę dokonać prawidłowego wyboru")
        print("o - orzeł")
        print("r - reszka")
        print("0 - koniec gry")
        continue

    y = random.choice(["orzeł", "reszka"])
    for i in range (0,3):
        print (3-i)
        time.sleep(1)
    print("wynik rzutu:", y)

    if x == y:
        user = user +1
    else:
        computer = computer +1

    print("wynik łącznie:")
    print("użytkownik:", user)
    print("komputer:", computer)


