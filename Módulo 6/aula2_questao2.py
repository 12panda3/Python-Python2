import random as rad

elementos = []
num_elementos = rad.randint(5, 20)
num_elementomedia = num_elementos

while num_elementos > 0:
    elementos.append(rad.randint(1, 10))
    num_elementos -= 1

soma = sum(elementos)

media = soma / num_elementomedia

print('lista de elementos ', elementos)
print('soma de itens da lista: ', soma)
print('media dos itens da lista: ', media)