#CRUD
from csv import *

def CRIAR(nome=None, senha=None, email=None, nivel=None):

    if nome is None:
        nome = str(input('Digite o nome do usuário à ser cadastrado: '))
    if senha is None:
        senha = str(input('Digite a senha do usuário à ser cadastrado: '))
    if email is None:
        email = str(input('Digite o email do usuário à ser cadastrado: '))
    if nivel is None:
        nivel = str(input('Digite o nivel de permissao do usuário: '))

    dadosNovoUser = []
    ids = []

    with open('users.csv', 'r', newline='') as x:
        next(x)
        arquivo = reader(x)
        
        for l in arquivo:
            if len(l) > 0:
                ids.append(int(l[0]))
    
    if len(ids) == 0:
        newId = 1
    else: 
        newId = max(ids) + 1

    dadosNovoUser = [newId, nome, senha, email, nivel]

    with open('users.csv', 'a', newline='') as x:
        escrita = writer(x)
        escrita.writerow(dadosNovoUser)

def LER():
    listaUsuarios = []

    with open('users.csv', 'r') as x:
        next(x)
        arquivo = reader(x)

        for i in arquivo:
            listaUsuarios.append(i)
    return listaUsuarios

def ATUALIZAR(iduser=None, nome=None, senha=None, email=None, nivel=None):
    listaLinhas = []
    
    with open('users.csv', 'r', newline='') as x:
        arquivo = reader(x)
        cabecalho = next(arquivo)
        for linha in arquivo:
            listaLinhas.append(linha)
            
    att = False
    for user in listaLinhas:
        if user[0] == str(iduser):
            if nome:
                user[1] = nome
            if senha:
                user[2] = senha
            if email:
                user[3] = email
            if nivel:
                user[4] = nivel
                
            att = True
            break
    
    if att == True:
         with open('users.csv', 'w', newline='') as x:
            nana = writer(x)
            nana.writerow(['ID do usuário', 'Nome', 'Senha', 'Email', 'Nivel'])
            nana.writerows(listaLinhas)

def EXCLUIR(iduser=None):
    if iduser is None:
        iduser = str(input("ID: "))
        
    listaLinhas = []
    
    with open('users.csv', 'r', newline='') as x:
        arquivo = reader(x)
        cabecalho = next(arquivo)
        
        for linha in arquivo:
            if linha and linha[0] != iduser:
                listaLinhas.append(linha)
        
    with open('users.csv', 'w', newline='') as x:
        nana = writer(x)
        nana.writerow(['ID', 'Nome', 'Senha', 'Email', 'Nivel'])
        nana.writerows(listaLinhas)


def CRIARPRODUTO(nomePrd=None, valorPrd=None, quantPrd=None):
    
    dadosNovoProduto = []
    idsPrd = []

    if nomePrd is None:
        nomePrd = str(input('Digite o nome do produto a ser adicionado: '))
    if valorPrd is None:
        valorPrd = str(input('Digite o valor do produto a ser adicionado: '))
    if quantPrd is None:
        quantPrd = str(input('Digite a quantidade do produto a ser adicionado: '))

    
    with open('produtos.csv', 'r', newline='') as x:
        next(x)
        arquivo = reader(x)

        for l in arquivo:
            if l:
                idsPrd.append(int(l[0]))
    
        if len(idsPrd) == 0:
            newId = 1
        else: 
            newId = max(idsPrd) + 1

        dadosNovoProduto.append(newId)
        dadosNovoProduto.append(nomePrd)
        dadosNovoProduto.append(valorPrd)
        dadosNovoProduto.append(quantPrd)

    with open('produtos.csv', 'a', newline='') as x:
        escrita = writer(x)
        escrita.writerow(dadosNovoProduto)

def LERPRODUTO():
    listaProds = []

    with open('produtos.csv', 'r') as x:
        next(x)
        arquivo = reader(x)

        for i in arquivo:
            listaProds.append(i)
    
        for linha in listaProds:
            print(linha, '\n')
    return listaProds

def ATUALIZARPRODUTO(prodId=None, nomeProd=None, valorProd=None, qntdProd=None):
    listaLinhas = []
            
    with open('produtos.csv', 'r', newline='') as x:
        arquivo = reader(x)
        cabecalho = next(arquivo)
        idAtt = input('Digite o ID do produto que deseja ser atualizado: ')

        for linha in arquivo:
            if linha:
                listaLinhas.append(linha)
                
    att = False
    
    for linha in listaLinhas:
        if linha[0] == str(prodId):
            if nomeProd:
                linha[1] = nomeProd
            if valorProd:
                linha[2] = valorProd
            if qntdProd:
                linha[3] = qntdProd
            att = True
            break
    
    if att == True:
        with open('produtos.csv', 'w', newline='') as x:
            nana = writer(x)
            nana.writerow(['ID do produto', 'Nome', 'Valor do produto', 'Quantidade'])
            nana.writerows(listaLinhas)

def EXCLUIRPRODUTO(idprod=None):
    listaLinhas = []

    with open('produtos.csv', 'r') as x:
        arquivo = reader(x)
        cabecalho = next(arquivo)
        for linha in arquivo:
            if linha and linha[0] != idprod:
                listaLinhas.append(linha)
        
    with open('produtos.csv', 'w', newline='') as x:
        nana = writer(x)
        nana.writerow(cabecalho)
        nana.writerows(listaLinhas)


def busca(buscando):
    with open('produtos.csv', 'r', newline='') as f:
        arquivo = reader(f)
        next(arquivo)

        resultados = [linha for linha in arquivo if buscando.lower() in linha[1].lower()]
    return resultados

def ordNome():
    with open('produtos.csv', 'r', newline='') as f:
        arquivo = reader(f)
        next(arquivo)
        items = list(arquivo)

    items.sort(key=lambda x: x[1].lower()) 
    return items

def ordPreco():
    with open('produtos.csv', 'r', newline='') as f:
        arquivo = reader(f)
        next(arquivo) 
        items = list(arquivo)

    items.sort(key=lambda x: float(x[2])) 
    return items
