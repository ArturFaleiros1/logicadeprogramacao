'''
Programa 02
Prof: Karython
Turma 2° DS

Sorteio 2.0
'''

import random
import time
import os

lista_nomes = []
lista_sorteados = []

print (30*"-", "Bem vindo ao sistema de sorteios", 30*"-")
while True:
    nome = input("Digite um nome para ser sorteado: ").title()
    lista_nomes.append(nome)
<<<<<<< HEAD
    opcao = input("Deseja adicionar mais s - Sim ou n - Não ")
=======
    opcao = input("Deseja adicionar mais s - Sim ou n - Não")
>>>>>>> 4a06411aea03906158ca56f0de663e12a8f02e27
    if opcao != "s":
        break

    while True:
        if not lista_nomes:
<<<<<<< HEAD
         print("A lista de nomes está vazia!")
=======
         print("A lsita de nomes está vazia!")
>>>>>>> 4a06411aea03906158ca56f0de663e12a8f02e27
        break
else:
    nome_sorteado = random.choice(lista_nomes)
    lista_sorteados.append(nome_sorteado)
