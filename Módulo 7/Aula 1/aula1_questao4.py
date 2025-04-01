numero = str(input('digite um numero de celular: '))
numeroCorrigido = str()

if len(numero) < 8:
    print('numero invalido')

for i in numero:
    if len(numero) == 8:
        numeroCorrigido = '9' + numero[0:4] + '-' + numero[4:8]
    else:
        if len(numero) == 9:
            numeroCorrigido = numero[0:5] + '-' + numero[5:9]

print(numeroCorrigido)

