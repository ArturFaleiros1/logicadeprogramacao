lista = ['gomes', ' fulano' , 'jesus', 'caio'  ,'felipe' , 'maria' , 'pedro', 'cicrano']


# imprimindo valor especifico da lista
print(lista[0])

#imprimindo o  ultimo indice
print(lista[-1])

#imprimir o valor
print(lista[2:4])

# ordenar essa lista
#lista.sort()

# adicionando na lista
lista.append('Karython')

#inserindo em posicao especifica
lista.insert(2, 'joao')

# inserindo varios valores
lista.extend(['Ana', 'Lucas', 'Eduardo' , 'Robert'])

n = []

# afivionando valores de forma dinamica 
# for i in range(10):
   # numeros.append(i * 2)
    # print(numeros)


# removendo item da lista
print(f'Lista antes de remover {lista}')

# pop - remove pelo indice
lista.pop(0)

# removendo o ultimo indice
lista.pop()

# removendo pelo valor
lista.remove('caio')

print(f'Lista depois de remover {lista}')

lista_numeros = [n for n in range(10)]
#removendo intervalo de valores
del lista_numeros[2:4]
print(f'Lista depois de remover {lista_numeros}')


listanomes = ["Gomes", "fulano", "cicrano", "beltrano", "maria", "pedro"]
# alterando o valor de lista
listanomes[1] = 'lucas'

print(listanomes)

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
        if numeros[i] > 5:
            numeros[i] = numeros[i] * 2
print(numeros)

# list compreheision
numeros = [n * 2 if n > 20 else n for n in numeros]
print(numeros)