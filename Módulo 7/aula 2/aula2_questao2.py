frase = str(input('digite uma frase: '))
fraseNova = ''

for i in frase:
    if i in 'aeiou':
        fraseNova = fraseNova + '*'
    else:
        fraseNova += i

print(fraseNova)