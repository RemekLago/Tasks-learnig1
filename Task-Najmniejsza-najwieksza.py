lista_liczb = [1,4,-4,7]

najmniejsza_liczba = None
najwieksza_liczba = None

for a in lista_liczb:
    if najmniejsza_liczba == None or najmniejsza_liczba > a:
        najmniejsza_liczba = a
    if najwieksza_liczba == None or najwieksza_liczba < a:
        najwieksza_liczba = a

print ("najmniejsza liczba to:", najmniejsza_liczba)
print ("najwieksza liczba to:", najwieksza_liczba)
