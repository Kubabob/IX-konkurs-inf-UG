

ilosc_zestawow = int(input())
flag = False

od_lewej = []
od_prawej = []
suma = 0
wejscie = list(map(int, input().split()))

if ilosc_zestawow > 1:
  flag = True

while True:
  try:
    if wejscie[0] < 0:
        wejscie = wejscie[1:]
    elif wejscie[-1] < 0:
        wejscie = wejscie[:-1]
    else:
        break
  except:
    break

if len(wejscie) == 0:
  zysk = 0
  
else:
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
  except:
    if flag:
      zysk = max(wejscie)
    else:
      zysk = 0

print(zysk)





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
