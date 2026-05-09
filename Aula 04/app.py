# for

# laco de for, é finitio: quando eu sei o numero de repeticoes
#frutas = ['melancia', 'abacaxi', 'melão' , 'pera']
#fruta = 'melancia'

#for f in frutas : 
 #   print(frutas[0])

#for range (inicio, tamanho, salto)

# for _ in range(1,20,2):
   # print("Repeti")   
# Input para um usuario digitar um número qualquer
'''num = int(input('Digite um número para saber a sua tabudada: '))
# aqui cria um laço de repetição finita, no caso ate 10, exibindo a tabuada
for i in range(1,11):
    print(f"{i} X {num} = {i * num}")'''



lista_nomes = ['José' 'Robervaldo', 'Nicollas ', 'Caio', ' Carlos', 'Maria', 'Rodrigo' 'Arthur Ribeiro', 'Natanael', ' Pedro', 'Bruno', 'Rian']
for i, nome  in enumerate(lista_nomes):
        print(f'{i+1}° {nome}')

nome_buscar = input(" Digite um nome para buscar: ").title()
        
if nome_buscar in lista_nomes:
                print("Usuário Encontrado! ")