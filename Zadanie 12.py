"""
Stwórz funkcję, która obsługuje otwieranie pliku do wczytywania danych.

Zapytaj się użytkownika o nazwę pliku, który chce otworzyć do wczytania.

Jeśli plik nie istnieje wypisz mu odpowiedni komunikat.

Jeśli plik istnieje wczytaj całą jego zawartość i zwróć jako wynik funkcji.

Podpowiedź: skorzystaj z wiedzy dotyczącej obsługi wyjątków z poprzedniej lekcji:

except FileNotFoundError:
"""

def file_reading(userfile):
    try:
        with open(userfile, "r", encoding="UTF-8") as file:
            return file.read()

    except FileNotFoundError:
        print("File name",userfile, "doesn't exist")

userfile = input("Hello, please write o file name to open: ")

file_print = file_reading(userfile)
print(file_print)

"""
def read_content_of_file(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Nie znaleziono pliku, podaj prawidłową ścieżkę")


nameOfFile = input("Podaj nazwę pliku do otwarcia: ")

fileContent = read_content_of_file(nameOfFile)
"""