while True:
    frase = input('digite uma frase (ou "fim" para encerrar) ')
    frase = frase.lower()
    frase = frase.replace(" ", '')
    
    if frase == 'fim':
        break

    if frase == frase[::-1]:
        print('a frase é um palindromo')
    else:
        print('a frase nao e um palindromo')

