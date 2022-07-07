import os
import json 
nomesCadastrados = []
cpfCadastrados = []
telefonesCadastrados = []
#Função para cadastro
def cadastro():
    print("====== C A D A S T R O =======")
    nome = input("Nome: ")
    nomesCadastrados.append(nome)
    cpf = input("CPF: ")
    cpfCadastrados.append(cpf)
    telefone = input("Telefone: ")
    telefonesCadastrados.append(telefone)
    print("Cadastro finalizado.")
    enviar(nome)
    voltar()


#Função para venda
def venda():
    print('''=========P R O D U T O S=========
    Seguros - conheça nossos planos!
    Previdência - entre em contato com a agência!
    Sei lá - pipipipopopo
    Camisetas - não disponível no momento''')
    voltar()

#Função voltar
def voltar():
    voltar = int(input('''Deseja  voltar?
        1 - sim
        2 - não\n'''))
    if voltar == 1:
        os.system("cls")
    escolha()

#Função de cabeçalho
def escolha():
    print('''Digite:
    1- para realizar cadastro;
    2 - para realizar compra;''')
    valor = int(input("Valor: "))
    if valor != 1 and valor != 2:
        print("Por favor, digite um valor correspondente às ações disponíveis!")
        escolha()
    elif valor == 1:
        cadastro()
    elif valor == 2:
        venda()

# Função enviar
def enviar(nome):
    import pika

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=('Nome: ' + nome))

print("========== LOJAS BTG ===========")
escolha()