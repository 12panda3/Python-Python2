import random as rad

lista1 = []
lista2 = []
interceccao = []
i = 20


def frequencia(lista):
    freq = {}
    for n in lista:
        if n in freq:
            freq[n] += 1

        else:
            freq[n] = 1

    return freq

while i > 0:
    lista1.append(rad.randint(0, 50))
    lista2.append(rad.randint(0, 50))
    i -= 1

interceccao = sorted(set(lista1) & set(lista2))

contlista1 = frequencia(lista1)
contlista2 = frequencia(lista2)


print('lista 1: ', lista1)
print('lista 2: ', lista2)
print('interccao: ', interceccao)

print('\n frequencia dos elementos na lista 2:')
for num, freq in contlista1.items():
    if freq > 1:
        print(f'{num}: {freq} vezes')

print('\n frequencia dos elementos na lista 1:')
for num, freq in contlista2.items():
    if freq > 1:
        print(f'{num}: {freq} vezes')
