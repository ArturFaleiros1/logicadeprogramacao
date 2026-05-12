import modulo as ma

def main():
   while True:
        print("Calculadora")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("5. Limpar terminal")

        opcao = input("Digite a opção digitada: ")
        match opcao:
            case '1':
                print('----- SOMA -----')
                num1 = int(input('Digite um número para somar: '))
                num2 = int(input('Digite outro número para somar: '))
                result = ma.soma(num1, num2)
                print(f'Resultado: {result}')
                break
            case '2':
                print('----- SUBTRAÇÃO  -----')
                num1 = int(input('Digite um número para subtrair: '))
                num2 = int(input('Digite outro número para subtrair: '))
                result = ma.sub(num1, num2)
                print(f'Resultado: {result}')
                break
            case '3':
                print('----- MULTPLICAÇÃO  -----')
                num1 = int(input('Digite um número para multiplicação: '))
                num2 = int(input('Digite outro número para multiplicação: '))
                result = ma.multiplicacao(num1, num2)
                print(f'Resultado: {result}')
                break
            case '4':
                print('----- Divisão   -----')
                num1 = int(input('Digite um número para dividir: '))
                num2 = int(input('Digite outro número para dividir: '))
                result = ma.divisao(num1, num2)
                print(f'Resultado: {result}')
                break
            case '5':
                ma.limpa_terminal()
                break
            case _ :
                print("Opção invalida")


           