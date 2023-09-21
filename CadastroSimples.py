'''Simples Sistema de Cadastro'''

# Importar as bibliotecas necessárias
import os


# Definir as funções necessárias

usuarios = []
senhas = []
emails = []

def menu():
    '''Mostra o Menu do sistema de cadastro.'''
    print('SISTEMA DE CADASTRO ')
    print('1. Cadastrar')
    print('2. Listar')
    print('3. Sair')
    opcao = input('Insira a opção desejada: ')
    return opcao

def cadastrar():
    print('Cadastro de Usuário')
    nome = input('Nome:').lower()
    usuarios.append(nome)
    senha = input('Senha: ').lower()
    senhas.append(senha)
    email = input('Email: ').lower()
    emails.append(email)
    print ()
    print('Usuário cadastrado com sucesso!')
    
def listar():
    print ('Lista de usuários: ')
    if len(usuarios) == 0:
        print('Não há usuários cadastrados.')
    else:
        print(f'Usuarios : {usuarios} e emails: {emails}')
        print()
            


#Programa principal

while True:
    
    opcao = menu()
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        print('Sistema finalizado, até logo!')
        break
    else:
        print('Opção invalida')        

                   