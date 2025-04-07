import random

tracejo = ''
letrasUsadas = []
chancesRestantes = 6

with open('gabarito_forca.txt', 'r') as linha:
    linhas = linha.readlines()
palavra = linhas[(random.randint(0, len(linhas) - 1))].strip().lower()

with open('gabarito_enforcado.txt', 'r', encoding='utf-8') as fig:
    desenhos = fig.readlines()

estagios = ["".join(desenhos[i:i+5]) for i in range(0, len(desenhos), 5)]

forca0 = estagios[0]
forca1 = estagios[1]
forca2 = estagios[2]
forca3 = estagios[3]
forca4 = estagios[4]
forca5 = estagios[5]
forca6 = estagios[6]

def imprime_enforcado(x):
    print(globals()[f"forca{x}"])

while True:
    estado = True

    for letra in palavra:
        if letra in letrasUsadas:
            print(letra, end = '')
        else:
            print('_', end = '')
            estado = False

    print(' ')

    if estado == True:
        print('voce ganhou dessa vez.')
        break

    chute = input('diga uma letra: ')
    chute = chute.lower()
    letrasUsadas.append(chute)

    for i in palavra:
        if i not in letrasUsadas:
            estado = False

    if chute not in palavra:
        chancesRestantes -= 1
        imprime_enforcado(6 - chancesRestantes)
        if chancesRestantes == 0:
            print('voce perdeu.')
            break


    