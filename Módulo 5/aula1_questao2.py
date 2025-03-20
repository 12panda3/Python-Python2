


import random, math

n = int(input('informe o número de valores a seren gerados: '))

lista = [random.randint(0, 100) for x in range(n)]

soma = sum(lista)

res = math.sqrt(soma)

print('A raíz quadrada dos valores somados é: ', round(res, 4))