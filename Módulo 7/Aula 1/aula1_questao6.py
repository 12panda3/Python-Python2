frase = str(input('digite sua frase: '))
palavraObjetivo = sorted(str(input('digite a palavra objetivo: ')))

lista = frase.lower().split()

for i in lista:
    if sorted(i) == palavraObjetivo:
        print(i)

