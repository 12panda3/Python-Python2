senha = str(input('insira sua senha: '))


def validador_senha(s):
    tamanho = maior = menor = numero = exp = False

    if len(s) >= 8:
        tamanho = True
    
    for i in s:
        if i.isdigit():
            numero = True

        if i in '@#!$%&.,:;':
            exp = True
        
        if i.isupper():
            maior = True

        if i.islower():
            menor = True

    return tamanho, maior, menor, numero, exp

tamanho, maior, menor, numero, exp = validador_senha(senha)

if tamanho and maior and menor and numero and exp == True :
    print('senha valida')
else:
    print('senha invalida')
