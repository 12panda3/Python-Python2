import re 

with open('frase.txt', 'r') as f:
    frase = f.read()

linhas = re.findall(r'[a-zA-ZÀ-ÖØ-öø-ÿ]+', frase)

with open('linhas.txt', 'w') as fraseLinhas:
    fraseLinhas.write('\n'.join(linhas))

with open('linhas.txt', 'r') as fraseLinhas:
    print(fraseLinhas.read())