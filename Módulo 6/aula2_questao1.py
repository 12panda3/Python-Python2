import random as rad

lista = []
z = []
o = 0

while len(lista) < 20:
    x = rad.randint(-100, 100)
    lista.append(x)
    z.append(x)

for i in lista:
    if i > o:
        o = i    


for i in lista:
    if i < o:
        e = i    

maI = lista.index(o)
meI = lista.index(e)

z.sort()
print('lista ordenada', z)
print('lista desordenada', lista)
print('maior indice da lista: ', maI, ' menor indice: ', meI)