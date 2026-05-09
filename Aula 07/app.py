'''
Manipulação de arquivos: oercorrer meus diretorios, encontrar o arquivo
passar o comendo de abertura de arquivo, passar o comando de ação 

arquivp = open('arquivo.txt',  'modo')

modos de ação:
    - "r" : leitura do arquivo
    - "w': escrita(sobrescreve o conteudo antido)
    - "a": adiciona o conteudo
    - "x": arquivo binarios
    - "t" : texto
'''

# Criando e escrevendo arquivo
arquivo = open('primeiro_arquivo.txt', "w")
arquivo.write('Olá arquivo! meu primeiro mundo')
arquivo.close()

# lendo arquivo
arquivo = open("primeiro_arquivo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# aplicando boa pratica
with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

    # arquivo com multiplas escrita
with open('alunos.txt', "a") as arquivo:
    arquivo.write('Ana\n')
    arquivo.write('Caio\n')
    arquivo.write('João\n')
    arquivo.write('Karython\n')
    arquivo.write('Gomes\n')
    arquivo.write('Fulano\n')
    
# lendo a linha a linha
with open('alunos.txt') as arquivo:
    for linha in arquivo:
        print(linha)

# usando lista para escrever no arquvo
frutas = ['pera', 'abacaxi', 'manga', 'caju']

with open('frutas.txt', "w") as arquivo:
    for f in frutas:
        arquivo.write(f + '\n')

# converter o arquivo em uma lista
with open('frutas.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

print(type(linhas))
print(linhas)

# Saída: ['pera\n', 'abacaxi\n', 'manga\n', 'caju\n']

#limpar a quebra de linha

with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())


# exemplo para cadastro

while True:
    nome = input("Digite seu nome: ").title()

    with open("cadastro.txt", "a") as arquivo:
        arquivo.write(nome + "\n")

    sair = input("Deseja sair? s/n: ").lower()

    if sair == 's':
        break