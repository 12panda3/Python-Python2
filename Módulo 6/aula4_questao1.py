lista1 = [x + 1 for x in range(19, 50, 2)]
print(lista1)

#########################################

lista2 = [x*x for x in range(1, 10)]
print(lista2)

#########################################

lista3 = [x for x in range(0, 100) if (x % 7) == 0]
print(lista3)

#########################################

lista4 = ['impar' if ((x % 2) != 0) else 'par' for x in range(0, 30, 3)]
print(lista4)