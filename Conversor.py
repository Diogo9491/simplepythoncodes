'''Conversor de Graus Celsius para Farenheit e vice-versa'''

#Funções de conversão
        
def converter_celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def converter_fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

#Menu do programa
def menu():
    '''Mostra o Menu do sistema de conversão Celsius para Fahrenheit.'''
    print('MENU ')
    print('1. Converter Celsius para Fahrenheit')
    print('2. Converter Fahrenheit para Celsius')
    print('3. Sair')
    print()
    opcao = input('Insira a opção desejada: ')
    return opcao

# Main
while True:
    print()
    opcao = menu()

    if opcao == '1':
        celsi = float(input('Insira a temperatura em Celsius: '))
        faren = converter_celsius_para_fahrenheit(celsi)
        print(f'O valor convertido para Fahrenheit é: {faren:.2f}')

    elif opcao == '2':
        faren = float(input('Insira a temperatura em Fahrenheit: '))
        celsi = converter_fahrenheit_para_celsius(faren)
        print(f'O valor convertido para Celsius é: {celsi:.2f}')

    elif opcao == '3':
        print('Programa Finalizado.')
        break

    else:
        print('Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).')

    
        
    
    
    
        