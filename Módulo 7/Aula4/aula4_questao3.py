import os
linhas = 0
maiorLinha = ''
cont, linhaMaior = 1, 0

f1 = open('estomago.txt', 'r', encoding='utf-8')
for i in range(25):
    print(f1.readline())

f2 = open('estomago.txt', 'r', encoding='utf-8')
for i in f2:
    linhas += 1
print('total de linhas: ', linhas)

f3 = open('estomago.txt', 'r', encoding='utf-8')
for i in f3:
    cont += 1
    if len(i) > len(maiorLinha):
        linhaMaior = cont
        maiorLinha = i
print('linha com maior tamanho: ', linhaMaior)

f4 = open('estomago.txt', 'r', encoding='utf-8')
import re

texto = f4.read()

nonato = re.findall(r'\bnonato\b', texto, flags=re.IGNORECASE)
iria = re.findall(r'\bíria\b', texto, flags=re.IGNORECASE)

print('quantidade de vezes que nonato e iria foram citados: ', len(nonato), ',', len(iria))