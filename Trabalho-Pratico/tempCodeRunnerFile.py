from tkinter import *
from tkinter import messagebox
import funcoes, janelas

def login():
    email = inputEmail.get()
    senha = inputSenha.get()
    user = funcoes.verificacao(email, senha)


    if user:
        messagebox.showinfo('Bem vindo', 'Bem vindo')
        janelaLogin.destroy()
        nivel = user[4]

        if nivel == '1':
            janelas.janelaAdmin()
            
        elif nivel == '2':
            janelas.janelaModerador()
        
        elif nivel == '3':
            janelas.janelaUser()
        
    else:
        messagebox.showinfo('Erro ao fazer login', 'Erro no email ou senha.')
        

janelaLogin = Tk()

janelaLogin.title('Login')

areaLogin = Label(janelaLogin, text='Login')
areaLogin.grid(column=1, row=0)

areaEmail = Label(janelaLogin, text='Insira o E-mail de usuário')
areaEmail.grid(column=0, row=1)
inputEmail = Entry(janelaLogin)
inputEmail.grid(column=2, row=1)

areaSenha = Label(janelaLogin, text='Insira a senha de usuário')
areaSenha.grid(column=0, row=2)
inputSenha = Entry(janelaLogin)
inputSenha.grid(column=2, row=2)

buttonEntrar = Button(janelaLogin, text='Entrar', command=login)
buttonEntrar.grid(column=2, row=4)

janelaLogin.mainloop()