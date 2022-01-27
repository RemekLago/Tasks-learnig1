print("Podaj swoją liczbę: ")
value = int(input())
absolute_value = abs(value)

if value > 0:
    print("Liczba jest dodatnia, jest ok")
elif value == 0:
    print("Podana wartość wynosi 0 i też jest ok")
else:
    print("Podana liczba jest ujemna \n"
          "Jej wartość bezwzględna wynosi: ", absolute_value)


