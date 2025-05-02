import tkinter, crud, funcoes
from tkinter import messagebox

def janelaAdmin():
    janelaAdmin = tkinter.Tk()

    janelaAdmin.title('Painel do administrador')

    #USUÁRIOS
    opcoesTexto = tkinter.Label(janelaAdmin, text='Escolha uma das opções:')
    opcoesTexto.grid(row=1, column=1)

    botaoCriarUser = tkinter.Button(janelaAdmin, text='Adicionar Usuários', command=funcoes.janelaAdicionarUsuario)
    botaoCriarUser.grid(row=2, column=1)

    botaoLerUser = tkinter.Button(janelaAdmin, text='Mostrar Usuários', command=lambda: funcoes.mostrarUser(janelaAdmin))
    botaoLerUser.grid(row=2, column=2)

    botaoAtualizarUser = tkinter.Button(janelaAdmin, text='Atualizar Usuários', command=funcoes.janelaAtualizarUsuario)
    botaoAtualizarUser.grid(row=2, column=3)

    botaoDeletarUser = tkinter.Button(janelaAdmin, text='Deletar Usuários', command=funcoes.janelaExcluirUsuario)
    botaoDeletarUser.grid(row=2, column=4)


    #PRODUTOS
    botaoCriarProduto = tkinter.Button(janelaAdmin, text='Adicionar Produtos', command=funcoes.janelaAdicionarProduto)
    botaoCriarProduto.grid(row=3, column=1)

    botaoLerProduto = tkinter.Button(janelaAdmin, text='Mostrar Produtos', command=lambda: funcoes.mostrarProduto(janelaAdmin))
    botaoLerProduto.grid(row=3, column=2)

    botaoAtualizarProduto = tkinter.Button(janelaAdmin, text='Atualizar Produtos', command=funcoes.janelaAtualizarProduto)
    botaoAtualizarProduto.grid(row=3, column=3)

    botaoBuscarProduto = tkinter.Button(janelaAdmin, text='Buscar Produto', command=funcoes.janelaBuscarProduto)
    botaoBuscarProduto.grid(row=4, column=1)
    
    botaoOrdenarNome = tkinter.Button(janelaAdmin, text='Ordenar por Nome', command=funcoes.janelaOrdenarProdutoPorNome)
    botaoOrdenarNome.grid(row=4, column=2)
    
    botaoOrdenarPreco = tkinter.Button(janelaAdmin, text='Ordenar por Preço', command=funcoes.janelaOrdenarProdutoPorPreco)
    botaoOrdenarPreco.grid(row=4, column=3)

    botaoDeletarProduto = tkinter.Button(janelaAdmin, text='Deletar Produtos', command=funcoes.janelaExcluirProduto)
    botaoDeletarProduto.grid(row=3, column=4)

    janelaAdmin.mainloop()
    
def janelaModerador():
    janelaModerador = tkinter.Tk()
    
    janelaModerador.title('Painel do moderador')
    
    #USUÁRIOS
    opcoesTexto = tkinter.Label(janelaModerador, text='Escolha uma das opções:')
    opcoesTexto.grid(row=1, column=1)

    botaoLerUser = tkinter.Button(janelaModerador, text='Mostrar Usuários', command=lambda: funcoes.mostrarUser(janelaModerador))
    botaoLerUser.grid(row=2, column=2)


    #PRODUTOS
    botaoCriarProduto = tkinter.Button(janelaModerador, text='Adicionar Produtos', command=funcoes.janelaAdicionarProduto)
    botaoCriarProduto.grid(row=3, column=1)

    botaoLerProduto = tkinter.Button(janelaModerador, text='Mostrar Produtos', command=lambda: funcoes.mostrarProduto(janelaModerador))
    botaoLerProduto.grid(row=3, column=2)

    botaoAtualizarProduto = tkinter.Button(janelaModerador, text='Atualizar Produtos', command=funcoes.janelaAtualizarProduto)
    botaoAtualizarProduto.grid(row=3, column=3)

    botaoBuscarProduto = tkinter.Button(janelaAdmin, text='Buscar Produto', command=funcoes.janelaBuscarProduto)
    botaoBuscarProduto.grid(row=4, column=1)
    
    botaoOrdenarNome = tkinter.Button(janelaAdmin, text='Ordenar por Nome', command=funcoes.janelaOrdenarProdutoPorNome)
    botaoOrdenarNome.grid(row=4, column=2)
    
    botaoOrdenarPreco = tkinter.Button(janelaAdmin, text='Ordenar por Preço', command=funcoes.janelaOrdenarProdutoPorPreco)
    botaoOrdenarPreco.grid(row=4, column=3)
        
    botaoDeletarProduto = tkinter.Button(janelaModerador, text='Deletar Produtos', command=funcoes.janelaExcluirProduto)
    botaoDeletarProduto.grid(row=3, column=4)

    janelaModerador.mainloop()

def janelaUser():
    janelaUser = tkinter.Tk()
    
    janelaUser.title('Painel do usuário')
    
    opcoesTexto = tkinter.Label(janelaUser, text='Escolha uma das opções:')
    opcoesTexto.grid(row=1, column=1)

    #PRODUTOS
    botaoLerProduto = tkinter.Button(janelaUser, text='Mostrar Produtos', command=lambda: funcoes.mostrarProduto(janelaUser))
    botaoLerProduto.grid(row=1, column=1)
    
    botaoBuscarProduto = tkinter.Button(janelaAdmin, text='Buscar Produto', command=funcoes.janelaBuscarProduto)
    botaoBuscarProduto.grid(row=4, column=1)

    botaoOrdenarNome = tkinter.Button(janelaAdmin, text='Ordenar por Nome', command=funcoes.janelaOrdenarProdutoPorNome)
    botaoOrdenarNome.grid(row=4, column=2)

    botaoOrdenarPreco = tkinter.Button(janelaAdmin, text='Ordenar por Preço', command=funcoes.janelaOrdenarProdutoPorPreco)
    botaoOrdenarPreco.grid(row=4, column=3)

    janelaUser.mainloop()
