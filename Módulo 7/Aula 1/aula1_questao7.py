import random as rand
lista = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]


def encrypt(lista):
    listaCrypt = []
    chave = (rand.randint(1, 10))

    for i in lista:
        nomeCrypt = "".join(chr(ord(o) + chave) for o in i) 
        listaCrypt.append(nomeCrypt)
            
    return listaCrypt, chave

listaCrypt, chave = encrypt(lista)


print(lista)
print(listaCrypt)
print('chave: ', chave)