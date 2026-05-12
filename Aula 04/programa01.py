<<<<<<< HEAD
'''Programa 01 -Aula 04 - 28/04
=======
'''Programa 01 -Aula 01 - 28/04
>>>>>>> 4a06411aea03906158ca56f0de663e12a8f02e27
    Nome : Artur Faleiros
    Turma 2° DS


    sORTEIO 1.0
'''

import time 
import random


lista_nomes = ['José' 'Robervaldo', 'Nicollas ', 'Caio', ' Carlos', 'Maria', 'Rodrigo' 'Arthur Ribeiro', 'Natanael', ' Pedro', 'Bruno', 'Rian']


lista_sorteados = []
sorteados = 0
while sorteados < 5:
    nome_sorteado = random.choice(lista_nomes) 
    print(f'Sorteado: {nome_sorteado}')
    lista_sorteados.append(nome_sorteado)
    print(f'Lista antes de remover {len(lista_nomes)}')
    lista_nomes.remove(nome_sorteado)
    print(f'Lista atualizada {len(lista_nomes)}')
    sorteados +=1

<<<<<<< HEAD
print("Fim do Programa")s
=======
print("Fim do Programa")
>>>>>>> 4a06411aea03906158ca56f0de663e12a8f02e27
