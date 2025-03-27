frase = input('Digite uma frase: ')
frase = frase.replace(" ", '')

vogais = [sorted([letra for letra in frase if letra in 'aeiou'])]
consoantes = [sorted([letra for letra in frase if letra not in 'aeiou'])]

print(vogais)
print(consoantes)
