lista = []
n = 10

print("adicione dez números à lista")
while n > 0:
    n -= 1
    lista.append(input())

print(lista)
print(lista[0:3])
print(lista[-2:1])
print(lista[::-1])
print(lista[::2])
print(lista[1::2])