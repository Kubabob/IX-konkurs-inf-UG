import random

def generator_losowych_liczb_w_rzedzie(ilosc, a, b):
    lista_losowych_liczb = []
    for i in range(ilosc):
        lista_losowych_liczb.append(f'{random.randint(a, b)} ')

    return lista_losowych_liczb

print(1000000)
print(generator_losowych_liczb_w_rzedzie(1000000, -1000, 1000))