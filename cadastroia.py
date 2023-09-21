import os
import msvcrt  # Módulo para lidar com entrada/saída no Windows

usuarios = []

def limpar_tela():
    """Limpa a tela do terminal no Windows."""
    msvcrt.system("cls")

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
    senha = input('Senha: ').lower()
    email = input('Email: ').lower()
    usuario = {'nome': nome, 'senha': senha, 'email': email}
    usuarios.append(usuario)
    print()
    print('Usuário cadastrado com sucesso!')
    
def listar():
    print('Lista de usuários: ')
    if len(usuarios) == 0:
        print('Não há usuários cadastrados.')
    else:
        for usuario in usuarios:
            print('Nome:', usuario['nome'])
            print('Senha:', usuario['senha'])
            print('Email:', usuario['email'])
            print()

# Programa principal
while True:
    limpar_tela()
    opcao = menu()
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        print('Sistema finalizado, até logo!')
        break
    else:
        print('Opção inválida')
