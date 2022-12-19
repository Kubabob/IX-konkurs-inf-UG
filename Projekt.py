import metody
import time

start_time = time.time()

#ilosc_zestawow = int(input())
ilosc_zestawow = 1000000


od_lewej = []
od_prawej = []
suma = 0
#wejscie = list(map(int, input().split()))
wejscie = list(map(int, metody.generator_losowych_liczb_w_rzedzie(1000000, -1000, 1000)))


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

try:
    zysk = od_prawej[1]
    index = 0

    for i in range(1,len(od_lewej)-1):
        if od_lewej[i-1] + od_prawej[i+1] > zysk:
            zysk = od_lewej[i-1] + od_prawej[i+1]
except IndexError:
    zysk = od_prawej[0]

print(zysk)

print(f'{time.time()-start_time}s')



"""
1
1 4 -7 2 -1 4

8
-1 2 7 -4 2 -1 5 -4

11 9 2 6 4 5
2  9 5 7 6 11

10
-1 2 -2 3 -4 -5 7 10 -2 8
"""
