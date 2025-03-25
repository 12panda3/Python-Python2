import random 
listaNumeros = [-10, -9, -7, -4, -5, 3, 2, 4, -1, -2, -3, -12]
inicioMaiorFatia, tamanhoMaiorFatia = 0, 0
inicioFatiaAtual, tamanhoFatiaAtual = 0, 0

for i in range(len(listaNumeros)):
    if listaNumeros[i] < 0:
        tamanhoFatiaAtual += 1
        if tamanhoFatiaAtual ==1:
            inicioFatiaAtual = i
    else:
        if tamanhoFatiaAtual > tamanhoMaiorFatia:
            tamanhoMaiorFatia = tamanhoFatiaAtual
            inicioMaiorFatia = inicioFatiaAtual
        tamanhoFatiaAtual = 0



print(listaNumeros)
del listaNumeros[inicioMaiorFatia:inicioMaiorFatia+tamanhoMaiorFatia]
print(listaNumeros)