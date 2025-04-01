frase = str(input('digite um frase: '))
espacos = 0

for i in frase:
    if i == ' ':
        espacos += 1
print('numero de espacos: ', espacos)