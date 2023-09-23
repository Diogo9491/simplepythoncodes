'''Jogo em Python para acertar o número aleátorio entre 1 a 100 com dicas.'''

import random

numero = random.randint(0,100)

#Funções MENU E CHUTE
def menu():
    print('ADVINHE O NÚMERO!')
    print('[1] Começar o jogo!')
    print ('[2] Finalizar Programa')
    opcao = input('->:')
    return opcao

def chutando_valor(chute):
    
    if chute > numero:
        return 10, 'Muito alto! Chute um número mais baixo. '
    elif chute < numero:
        return 1, 'Muito baixo! Chute um número mais alto. '
    elif chute == numero:
        return  0, 'Parabéns! Você acertou! Fim de jogo.'
       


#MAIN
opcao = menu()
while True:
    
    if opcao == '1':
        chute = int(input('Faça seu chute: '))
        if chutando_valor(chute)[0] == 0:
            print(chutando_valor(chute)[1])
            break 
        else:
            print(chutando_valor(chute)[1])

    
    elif opcao == '2':
        print ('Programa finalizado! ')
        break
             