baza_liczb = [4, 19, 8, 7, 2, 11, 15, 19 ]

def sortowanie_babelkowe(baza_liczb):

    n = len(baza_liczb)

    while n > 1:

        for x in range(0, len(baza_liczb)-1):
            if baza_liczb[x] > baza_liczb[x+1]:
                baza_liczb[x], baza_liczb[x+1] = baza_liczb[x+1], baza_liczb[x]

        n -= 1
        print(baza_liczb)

    return baza_liczb

sortowanie_babelkowe(baza_liczb)