# Formulario-por-email
#Aplicação windows simples para fins de estudo.
#Autor: Thiago Martins Carvalho de Medeiros
#Contato: https://www.linkedin.com/in/thiago-carvalho-2020/

import smtplib
import tkinter
from tkinter import *


def adicionar():
    arquivo = open("Dados.csv", "a")
    arquivo.write(nome.get() + "   ")
    arquivo.write(idade.get() + "   ")
    arquivo.write(altura.get() + "\n")
    arquivo.close()

def enviar_email():
    arquivo = open("Dados.csv", "r")
    informacao = arquivo.read()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("digiteousuario@gmail.com", "digiteasenha")
    server.sendmail(
        "digiteoremetente@gmail.com",
        "digiteodestinatario@email.com",
        informacao)
    server.quit()

janela = Tk()
janela.title("Pesquisa de Estatura")

nome = tkinter.StringVar()
idade = tkinter.StringVar()
altura = tkinter.StringVar()

nometexto = tkinter.Label(janela, text="  Digite o nome: ")
idadetexto = tkinter.Label(janela, text="  Digite a idade: ")
alturatexto = tkinter.Label(janela, text="  Digite a altura: ")
nometexto.grid(column=0, row=1)
idadetexto.grid(column=0, row=2)
alturatexto.grid(column=0, row=3)
nome = tkinter.Entry(janela, width=20, textvariable=nome)
idade = tkinter.Entry(janela, width=20, textvariable=idade)
altura = tkinter.Entry(janela, width=20, textvariable=altura)
nome.grid(column=1, row=1, padx=20)
idade.grid(column=1, row=2, padx=20)
altura.grid(column=1, row=3, padx=20)

adicionar = tkinter.Button(janela, text="Adicionar", command=adicionar)
adicionar.grid(column=0, row=4)

enviar = tkinter.Button(janela, text="Enviar", command=enviar_email)
enviar.grid(column=1, row=4)

janela.mainloop()