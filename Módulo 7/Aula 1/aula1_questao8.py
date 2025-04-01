cpf = input('digite um cpf (XXX.XXX.XXX-XX): ')
multiplicadores = (10, 9, 8, 7, 6, 5, 4, 3, 2)
primeiros = cpf[:11].replace('.', '').replace('-', '') 
primeiroDigito = 0

for i in range(9):
    primeiroDigito += int(primeiros[i]) *multiplicadores[i] 

primeiroDigito = (primeiroDigito *10) %11  
primeiroDigito = 0 if primeiroDigito >=10 else primeiroDigito  

primeiros += str(primeiroDigito)
print('primeiro digito: ', primeiroDigito)

multiplicadores2 = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
segundoDigito = 0

for i in range(10):
    segundoDigito += int(primeiros[i]) *multiplicadores2[i] 

segundoDigito = (segundoDigito *10) %11  
segundoDigito = 0 if segundoDigito >=10 else segundoDigito  


print('segundo digito: ', segundoDigito)

cpfExtraido = cpf.replace('.', '').replace('-', '')

primeiros = primeiros +str(segundoDigito) 


if cpfExtraido == primeiros:
    print('cpf valido')
else:
    print('cpf invalido')