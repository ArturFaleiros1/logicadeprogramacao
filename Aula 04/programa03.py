
'''
sistema : calculadora
'''

while True:
    print(30*"-", "Calculadora", 30*"-")
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    opcao = input("Digite a operação: ")

    match opcao  :
        case '1' :
            resultado = num1 + num2
            print(f'{num1} + {num2} = {resultado}')
            break
        case '2':
            resultado = num1 - num2
            print(f'{num1} - {num2} = {resultado}')
            break
        case '3' :
            if num1 != 0 and num2 != 0:
                resultado = num1 * num2
            print(f'{num1} * {num2} = {resultado}')
            break
        case '4' :
            resultado = num1 / num2
            print(f'{num1} / {num2} = {resultado}')
            pass
        case _ :
            print("Digite um número valido ")
            pass
