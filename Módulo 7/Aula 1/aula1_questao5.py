frase = str(input('digite uma frase: '))
vogais = 0
indices = []

for i in frase:
    if i in 'aeiou':
        vogais += 1
        indices.append(frase.index(i))

print(vogais, 'vogais')
print('indices das vogais: ', indices)