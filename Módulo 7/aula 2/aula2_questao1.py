data = str(input('digite a sua data de nascimento (dd/mm/aaaa): '))
meses = ('janeiro', 'fevereiro', 'março', 'abril', 
         'maio', 'junho', 'julho', 'agosto', 
         'setembro', 'outubro', 'novembro', 'dezembro')
dataSeparada = data.split('/')

mes = int(dataSeparada[1])


for i in meses:
    mesNome = meses[mes - 1]
print('sua data de nascimento é', dataSeparada[0], ' de ', mesNome, ' de ', dataSeparada[2])