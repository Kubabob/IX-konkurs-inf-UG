ile_pomiarow = int(input())

roznice = []
index_max = []
max_lokalne = []


for pomiar in range(ile_pomiarow):
    try:
        wejscie = list(map(int, input().split()))

        if wejscie[1] > wejscie[0]:
            roznice = [0,1]
            index_max = [0,1]
            max_lokalne = [wejscie[0],wejscie[1]]
        else:
            roznice = [0,0]
            index_max = [0]
            max_lokalne = [wejscie[0]]


        index = 1
        for liczba in wejscie[2:]:
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
                for i in range(index-1, wejscie.index(max_lokalne[-1])-1, -1):

                    if liczba > wejscie[i]:
                        suma_roznicy += 1
                    else:
                        roznice.append(suma_roznicy)


    except:
        print(*roznice)
        break


