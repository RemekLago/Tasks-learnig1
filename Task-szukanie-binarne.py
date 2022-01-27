def szukanie(lista, szukana_liczba):

    left = 0
    right = len(lista)
    index = 0

    while left < right:
        index = (left + right) //2
        if lista[index] == szukana_liczba:
            return index
        else:
            if lista[index] < szukana_liczba:
                left = index + 1
            else:
                right = index

    return -1

lista = [1,3,5,7,9,11,15,16,17,19]
szukana_liczba = 9
index = szukanie(lista, szukana_liczba)

print("szukana liczba ma index:", index)

