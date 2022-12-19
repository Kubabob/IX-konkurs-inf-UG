liczba_zestawow = int(input())
odp = []


def reszta_z_5(liczba):
    return liczba % 5

for zestaw in range(liczba_zestawow):
    wejscie_bin = input()
    ile = 0
    if wejscie_bin[0] == '0':
        suma = 0
        ile+=1
    else:
        suma = 1
    for cyfra in wejscie_bin[1:]:
        if cyfra == '0':
            suma = reszta_z_5(suma) * 2
        else:
            suma = reszta_z_5(suma) * 2 + 1
        if reszta_z_5(suma) == 0:
          ile+=1
    odp.append(ile)

for odpowiedz in odp:
    print(f'{odpowiedz}')