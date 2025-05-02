import csv, crud, tkinter
from tkinter import ttk, messagebox

def verificacao(email, senha, banco='users.csv'):
    with open(banco, 'r') as f:
        arquivo = csv.reader(f)
        next(arquivo)

        for l in arquivo:
            if l[3] == email and l[2] == senha:
                return l
    return None

def janelaBusca():
    janela = tkinter.Toplevel()
    janela.title("Buscar Produto por Nome")

    tkinter.Label(janela, text="Nome do produto:").grid(row=0, column=0, padx=5, pady=5)
    entryNome = tkinter.Entry(janela)
    entryNome.grid(row=0, column=1, padx=5, pady=5)

    def buscar():
        nome = entryNome.get()
        if not nome:
            messagebox.showerror("Erro", "Informe um nome para buscar.")
            return

        resultados = crud.BUSCARPRODUTOporNome(nome)
        if not resultados:
            messagebox.showinfo("Nenhum resultado", "Nenhum produto encontrado com esse nome.")
            return

        tabela = ttk.Treeview(janela, columns=('ID', 'Nome', 'Valor', 'Quantidade'), show='headings')
        for col in ('ID', 'Nome', 'Valor', 'Quantidade'):
            tabela.heading(col, text=col)

        for linha in resultados:
            tabela.insert('', 'end', values=linha)

        tabela.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    tkinter.Button(janela, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=5)

def janelaOrdNome():
    janela = tkinter.Toplevel()
    janela.title("Produtos Ordenados por Nome")

    produtos_ordenados = crud.ORDENARPRODUTOporNome()

    tabela = ttk.Treeview(janela, columns=('ID', 'Nome', 'Valor', 'Quantidade'), show='headings')
    for col in ('ID', 'Nome', 'Valor', 'Quantidade'):
        tabela.heading(col, text=col)

    for linha in produtos_ordenados:
        tabela.insert('', 'end', values=linha)

    tabela.pack(padx=10, pady=10)

def janelaOrdPreco():
    janela = tkinter.Toplevel()
    janela.title("Produtos Ordenados por Preço")

    produtos_ordenados = crud.ORDENARPRODUTOporPreco()

    tabela = ttk.Treeview(janela, columns=('ID', 'Nome', 'Valor', 'Quantidade'), show='headings')
    for col in ('ID', 'Nome', 'Valor', 'Quantidade'):
        tabela.heading(col, text=col)

    for linha in produtos_ordenados:
        tabela.insert('', 'end', values=linha)

    tabela.pack(padx=10, pady=10)

def abrirJanela(nivel):
    if nivel == 1:
        print()

    if nivel == 2:
        print()

    if nivel == 3:
        print()
        
def mostrarUser(janela):
    dados = crud.LER()
    
    tabela = ttk.Treeview(janela, columns=('ID', 'Nome de usuário', 'Email', 'Nível'), show='headings')
    
    tabela.heading('ID', text='ID')
    tabela.heading('Nome de usuário', text='Nome')
    tabela.heading('Email', text='Email')
    tabela.heading('Nível', text='Nivel')
    
    for linha in dados:
        tabela.insert('', 'end', values=linha)
    
    tabela.grid(row=4, column=0, columnspan=5, padx=10, pady=10)
    
def criarUser(nome, senha, email, nivel):
    with open('users.csv', 'r', newline='') as f:
        next(f)
        
        file = csv.reader(f)
        ids = [int(x[0]) for x in file if len(x) > 0]
    
    idnovo = max(ids) + 1 if ids else 1
    dados = [idnovo, nome, senha, email, nivel]
    
    with open('users.csv', 'a', newline='') as x:
        linha = csv.writer(x)
        linha.writerow(dados)
    
def mostrarProduto(janela):
    dados = crud.LERPRODUTO()
    
    tabela = ttk.Treeview(janela, columns=('ID do produto', 'Nome do produto', 'Valor', 'Quantidade'), show='headings')
    
    tabela.heading('ID do produto', text='ID do produto')
    tabela.heading('Nome do produto', text='Nome do produto')
    tabela.heading('Valor', text='Valor')
    tabela.heading('Quantidade', text='Quantidade')
    
    for linha in dados:
        tabela.insert('', 'end', values=linha)
    
    tabela.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

def janelaAdicionarUsuario():
    janelaAdd = tkinter.Toplevel()
    janelaAdd.title('Adicionar Usuário')

    tkinter.Label(janelaAdd, text='Nome:').grid(row=0, column=0)
    entryNome = tkinter.Entry(janelaAdd)
    entryNome.grid(row=0, column=1)

    tkinter.Label(janelaAdd, text='Senha:').grid(row=1, column=0)
    entrySenha = tkinter.Entry(janelaAdd, show='*')
    entrySenha.grid(row=1, column=1)

    tkinter.Label(janelaAdd, text='Email:').grid(row=2, column=0)
    entryEmail = tkinter.Entry(janelaAdd)
    entryEmail.grid(row=2, column=1)

    tkinter.Label(janelaAdd, text='Nível (1/2/3):').grid(row=3, column=0)
    entryNivel = tkinter.Entry(janelaAdd)
    entryNivel.grid(row=3, column=1)

    def salvar():
        nome = entryNome.get()
        senha = entrySenha.get()
        email = entryEmail.get()
        nivel = entryNivel.get()

        if nome and senha and email and nivel:
            crud.CRIAR(nome, senha, email, nivel)
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
            janelaAdd.destroy()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    botaoSalvar = tkinter.Button(janelaAdd, text='Salvar', command=salvar)
    botaoSalvar.grid(row=4, column=0, columnspan=2, pady=10)
    
def janelaAdicionarProduto():
    janelaAdd = tkinter.Toplevel()
    janelaAdd.title('Adicionar Produto')

    tkinter.Label(janelaAdd, text='Nome do Produto:').grid(row=0, column=0)
    entryNome = tkinter.Entry(janelaAdd)
    entryNome.grid(row=0, column=1)

    tkinter.Label(janelaAdd, text='Valor:').grid(row=1, column=0)
    entryValor = tkinter.Entry(janelaAdd)
    entryValor.grid(row=1, column=1)

    tkinter.Label(janelaAdd, text='Quantidade:').grid(row=2, column=0)
    entryQuantidade = tkinter.Entry(janelaAdd)
    entryQuantidade.grid(row=2, column=1)

    def salvar():
        nome = entryNome.get()
        valor = entryValor.get()
        quantidade = entryQuantidade.get()

        if nome and valor and quantidade:
            crud.CRIARPRODUTO(nome, valor, quantidade)
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            janelaAdd.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    tkinter.Button(janelaAdd, text='Salvar', command=salvar).grid(row=3, column=0, columnspan=2, pady=10)
    
def janelaAtualizarUsuario():
    janela = tkinter.Toplevel()
    janela.title('Atualizar Usuário')

    tkinter.Label(janela, text='ID do Usuário:').grid(row=0, column=0)
    entryId = tkinter.Entry(janela)
    entryId.grid(row=0, column=1)

    tkinter.Label(janela, text='Novo Nome (opcional):').grid(row=1, column=0)
    entryNome = tkinter.Entry(janela)
    entryNome.grid(row=1, column=1)

    tkinter.Label(janela, text='Nova Senha:').grid(row=2, column=0)
    entrySenha = tkinter.Entry(janela)
    entrySenha.grid(row=2, column=1)

    tkinter.Label(janela, text='Novo Email:').grid(row=3, column=0)
    entryEmail = tkinter.Entry(janela)
    entryEmail.grid(row=3, column=1)

    tkinter.Label(janela, text='Novo Nível:').grid(row=4, column=0)
    entryNivel = tkinter.Entry(janela)
    entryNivel.grid(row=4, column=1)

    def atualizar():
        id_usuario = entryId.get()
        nome = entryNome.get()
        senha = entrySenha.get()
        email = entryEmail.get()
        nivel = entryNivel.get()

        if not id_usuario:
            messagebox.showerror("Erro", "ID é obrigatório.")
            return

        crud.ATUALIZAR(id_usuario, nome, senha, email, nivel)
        messagebox.showinfo("Sucesso", "Usuário atualizado.")
        janela.destroy()

    tkinter.Button(janela, text='Atualizar', command=atualizar).grid(row=5, column=0, columnspan=2, pady=10)
    
def janelaAtualizarProduto():
    janela = tkinter.Toplevel()
    janela.title('Atualizar Produto')

    tkinter.Label(janela, text='ID do Produto:').grid(row=0, column=0)
    entryId = tkinter.Entry(janela)
    entryId.grid(row=0, column=1)

    tkinter.Label(janela, text='Novo Nome (deixe em branco para manter):').grid(row=1, column=0)
    entryNome = tkinter.Entry(janela)
    entryNome.grid(row=1, column=1)

    tkinter.Label(janela, text='Novo Valor:').grid(row=2, column=0)
    entryValor = tkinter.Entry(janela)
    entryValor.grid(row=2, column=1)

    tkinter.Label(janela, text='Nova Quantidade:').grid(row=3, column=0)
    entryQtd = tkinter.Entry(janela)
    entryQtd.grid(row=3, column=1)

    def atualizar():
        id_produto = entryId.get()
        nome = entryNome.get()
        valor = entryValor.get()
        qtd = entryQtd.get()

        if not id_produto:
            messagebox.showerror("Erro", "ID é obrigatório.")
            return

        crud.ATUALIZARPRODUTO(id_produto, nome, valor, qtd)
        messagebox.showinfo("Sucesso", "Produto atualizado.")
        janela.destroy()

    tkinter.Button(janela, text='Atualizar', command=atualizar).grid(row=4, column=0, columnspan=2, pady=10)
    
def janelaExcluirUsuario():
    janela = tkinter.Toplevel()
    janela.title("Excluir Usuário")

    tkinter.Label(janela, text="ID do Usuário:").grid(row=0, column=0, padx=5, pady=5)
    entryId = tkinter.Entry(janela)
    entryId.grid(row=0, column=1, padx=5, pady=5)

    def excluir():
        id_usuario = entryId.get()
        if not id_usuario:
            messagebox.showerror("Erro", "Informe o ID do usuário.")
            return

        crud.EXCLUIR(id_usuario)
        messagebox.showinfo("Sucesso", "Usuário excluído com sucesso.")
        janela.destroy()

    tkinter.Button(janela, text="Excluir", command=excluir).grid(row=1, column=0, columnspan=2, pady=10)
    
def janelaExcluirProduto():
    janela = tkinter.Toplevel()
    janela.title("Excluir Produto")

    tkinter.Label(janela, text="ID do Produto:").grid(row=0, column=0, padx=5, pady=5)
    entryId = tkinter.Entry(janela)
    entryId.grid(row=0, column=1, padx=5, pady=5)

    def excluir():
        id_produto = entryId.get()
        if not id_produto:
            messagebox.showerror("Erro", "Informe o ID do produto.")
            return

        crud.EXCLUIRPRODUTO(id_produto)
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso.")
        janela.destroy()

    tkinter.Button(janela, text="Excluir", command=excluir).grid(row=1, column=0, columnspan=2, pady=10)