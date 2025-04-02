import random

frase = input('digite sua frase: ')
fraseFinal = []

def embaralhar_palavras(f):

    fraseDividida = f.split(' ')
    for i in fraseDividida:
        meio = list(i[1:-1])
        random.shuffle(meio)
        fraseRandom = i[0] + ''.join(meio) + i[-1]

        fraseFinal.append(fraseRandom)
    
    return ' '.join(fraseFinal)

print(embaralhar_palavras(frase))


    

