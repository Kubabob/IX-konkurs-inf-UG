ilosc_zestawow = int(input())


od_lewej = []
od_prawej = []
suma = 0
wejscie = list(map(int, input().split()))

while True:
    if wejscie[0] < 0:
        wejscie = wejscie[1:]
    elif wejscie[-1] < 0:
        wejscie = wejscie[:-1]
    else:
        break

for liczba in wejscie:
    suma += liczba
    if suma < 0:
        od_lewej.append(0)
        suma = 0
    else:
        od_lewej.append(suma)

suma = 0
for liczba in wejscie[::-1]:
    suma += liczba
    if suma < 0:
        od_prawej.append(0)
        suma = 0
    else:
        od_prawej.append(suma)

od_prawej = od_prawej[::-1]

zysk = od_prawej[1]
index = 0

for i in range(1,len(od_lewej)-1):
    if od_lewej[i-1] + od_prawej[i+1] > zysk:
        zysk = od_lewej[i-1] + od_prawej[i+1]

print(zysk)



"""
1
1 4 -7 2 -1 4

8
-1 2 7 -4 2 -1 5 -4

11 9 2 6 4 5
2  9 5 7 6 11
"""