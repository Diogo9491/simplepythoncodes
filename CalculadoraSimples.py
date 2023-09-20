'''CALCULADORA SIMPLES EM PYTHON'''

print ('CALCULADORA SIMPLES!\n\n')

#Funções

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divi(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: divisão por zero"
    
#Loop para continuar solicitando valores até o usuário decidir parar

while True:
    
    
    valor1 = float(input('DIGITE [0] PARA SAIR! \nDigite o primeiro valor:  '))
    if valor1 == 0:
        print ('Programa finalizado.')
        break
    valor2 = float(input('Insira o segundo valor: '))   
    
    operacao = input('Insira a operação que deseja fazer: \n[1] = Soma\n[2] = Subtração\n[3] = Multiplicação\n[4] = Divisão\n[0] = Sair\n')

#Utilizando estrutura match case para substituir uso de if/ elif.
    match operacao:
        case '1':
            resultado = soma(valor1,valor2)
            print(f'Resultado da soma: {resultado}')
        case '2':
            resultado = sub(valor1,valor2)
            print(f'Resultado da soma: {resultado}')
        case '3':
            resultado = multi(valor1,valor2)
            print(f'Resultado da soma: {resultado}')        
        case '4':
            resultado = divi(valor1,valor2)
            print(f'Resultado da soma: {resultado}')
        case '0':
            print ('Programa FINALIZADO!')
            break        
        case _:
            print('Valor incorreto, escolha uma das opções!!')  
            
                