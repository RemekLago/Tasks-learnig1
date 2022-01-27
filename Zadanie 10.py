"""
def suma_liczb(*liczby):
    print(liczby)
    suma = 0
    for liczba in liczby:
        suma += liczba
    print(suma)


suma_liczb(2, 4, 1, 2, 4, 5, 10)
"""

def count(*arg):
    suma = 0
    for i in tuple(arg):
        suma = suma + i
    return suma
print(count(2, 4, 1, 2, 4, 5, 10))

print(count(2, 4, 1, 2, 4, 5, 10))