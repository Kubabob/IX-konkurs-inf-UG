def zrob_wielokat(lista):
    lista.sort(reverse=True)
    while True:
        try:
            if int(sum(lista[1:])) > lista[0]:
                return int(sum(lista))
            else:
                lista = lista[1:]
        except:
            return 0

odpowiedzi = []

liczba_zestawow = int(input())

for zestaw in range(liczba_zestawow):
    liczba_przesel = int(input())
    lista_przesel = list(map(int, input().split()))

    odpowiedzi.append(zrob_wielokat(lista_przesel))

for odp in odpowiedzi:
    print(odp)
