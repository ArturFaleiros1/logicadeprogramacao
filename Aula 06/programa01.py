'''
1 - Crie um programa que o ususario possa idigitar quantos numeros quiser e ao terminar imprima a lista em ordem crescente

2 - crie um programa que o usuario possa digitar a quantidade desejada de notas de um determinado aluno (nota minima 0 e nota maxima 10 e o programa calcula  a media desse aluno, e ao final imprima se o aluno esta (aprovado, reprovado ou recuperação))
'''

#Programa 01
lista_numeros = []

while True:
    numero = int(input("Digite um número qualquer: "))
    lista_numeros.append(numero)
    op = input("Deseja adicionar mais numero s - sim e n - não: ")
    if op != "s":
     break

lista_numeros.sort()
print(f"A lista em ordem crescente é {lista_numeros} ")
