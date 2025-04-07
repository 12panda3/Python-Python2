import os

frase = str(input('digite uma frase: '))
with open('frase.txt', 'w') as f:
    f.write(frase)
local = os.path.abspath('frase.txt')
print('frase  salva em', local)