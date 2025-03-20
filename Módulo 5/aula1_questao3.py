


import random as rad

n = int(rad.randint(0, 10))

while True:

    i = int(input('Dê um palpite do número gerado!: '))

    if i == n:
        print('Você acertou!')
        break 

    elif i > n:
        print("Palpite muito alto!")

    elif i < n:
        print('Palpite muito baixo!')