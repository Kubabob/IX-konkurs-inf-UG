ile_pomiarow = int(input())

roznice = [0]
index_max = [0]


wejscie = list(map(int, input().split()))

max_lokalne = [wejscie[0]]

index = 0
for liczba in wejscie[1:]:
  index += 1
  ile_max = 0
  for maximum in max_lokalne[::-1]:
    if liczba > maximum:
      ile_max += 1
    else:
      break
  if ile_max:
    roznice.append(index - wejscie.index(max_lokalne[-ile_max]))
    index_max.append(index)
    max_lokalne.append(liczba)
  else:
    suma_roznicy = 0

    sprawdzanie = False

    if liczba > wejscie[index-1]:
      sprawdzanie = True
    else:
      roznice.append(suma_roznicy)

    if sprawdzanie:
      for i in range(index-1, wejscie.index(max_lokalne[-1]) -1, -1):
        if liczba > wejscie[i]:
          suma_roznicy += 1
        else:
          roznice.append(suma_roznicy)
    

print(*roznice)
