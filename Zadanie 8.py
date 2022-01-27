import time



liczba = int(input("Podaj liczbę: "))

def sumuj_do(liczba):
    suma = 0

    for liczba in range(1, liczba+1):
        suma = suma + liczba

    return suma

print(sumuj_do(liczba))

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba+1)])

print(sumuj_do2(liczba))

def sumuj_do3(liczba):
    return (1+liczba) / 2 * liczba

start = time.perf_counter()
print(sumuj_do3(liczba))
end = time.perf_counter()
print(end - start)