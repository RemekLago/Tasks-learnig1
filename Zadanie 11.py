"""
def choose_random_numbers(amount, total_amount):
    print(rando.sample(range(total_amount + 1), amount))

choose_random_numbers(6,49)
"""
import random
from collections import Counter

#body_of_numbers = list()
#for i in range(1,50):
#    body_of_numbers.append(i)
#print(body_of_numbers)

"""
def random_list(how_many_numbers, body_of_numbers):
    final_list = []
    i = 0
    while i < 6:
        win_list = random.randint(1, body_of_numbers)
        if win_list not in final_list:
            final_list.append(win_list)
            i = i + 1
        else:
            continue
    return final_list
print(random_list(6,50))
"""

def random_list(how_many_numbers, body_of_numbers):
    final_list = []
    i = 0
    for i in range(0,how_many_numbers):
        win_list = random.randint(1, body_of_numbers)
        final_list.append(win_list)
        if win_list not in final_list:
            i = i + 1
        else:
            continue
    return final_list
print(random_list(6,50))


""""
x = 0
wylosowane_liczby = list()
while x < 100:
    x = x + 1
    wylosowane_liczby.append(random.sample(range(1,50),6))
#    print("W tym losowaniu szczęśliwe liczby to: ", wylosowane_liczby)
    druk_wylosowane = Counter(wylosowane_liczby) # chcę zliczyć ile razy dana liczba została wylosowana podczas tych 100 losowań

print(druk_wylosowane)
"""