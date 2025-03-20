lista1 = []
lista2 = []
lista3 = []

print('digite o número de elementos na lista: ')
index1 = int(input())

print('digite os números dentro da lista:')
while index1 > 0:
    lista1.append(int(input()))
    index1 -= 1
print(lista1)

print('digite o número de elementos na segunda lista: ')
index2 = int(input())

print('digite os números dentro da segunda lista:')
while index2 > 0:
    lista2.append(int(input()))
    index2 -= 1
print(lista2)

for x, z in zip(lista1, lista2):
    lista3.append(x)
    lista3.append(z)

lista3.extend(lista1[len(lista3)//2:])
lista3.extend(lista2[len(lista3)//2:])

print('Lista intercalada:', lista3)