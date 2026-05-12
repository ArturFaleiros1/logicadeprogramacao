import time
import os
carros = []
proximo_id = 1
lista_carro = 'catalogo_carro.txt'

# Verifica se o arquivo existe, se não existir ele cria
if not os.path.exists(lista_carro):
    with open(lista_carro, 'w') as arquivo:
        pass

# le o arquivo txt e carrega a lista dos carros
with open(lista_carro, 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            partes = linha.split('|')
            carro = {
                'id'    : int(partes[0]),
                'modelo': partes[1],
                'preco' : float(partes[2]),
                'marca' : partes[3]
            }
            # garante que o id não esteja duplicado ou com o mesmo id quando executar o sistema denovo
            carros.append(carro)
            if carro['id'] >= proximo_id:
                proximo_id = carro['id'] + 1
 
while True:
    print("====== Sistema de carros ======")
    print('1 - Cadastrar carro')
    print('2 - Listar carros')
    print('3 - Atualizar carro')
    print('4 - Deletar carro')
    print('0 - Sair')
 
    opcao = input("Escolha uma opção: ")
 
    # Criar
    if opcao == '1':
        modelo = input("Digite o modelo do carro: ").title()
        preco = float(input("Digite o preço do carro: "))
        marca = input("Digite a marca do carro: ").title()
 
        carro = {
            'id'     : proximo_id,
            'modelo' : modelo,
            'preco'  : preco,
            'marca'  : marca
        }
 
        carros.append(carro)
        proximo_id += 1
        with open(lista_carro, 'a') as arquivo:
                 arquivo.write(f"{carro['id']}|{carro['modelo']}|{carro['preco']}|{carro['marca']}\n")

        print("✅ Carro cadastrado com sucesso!")
 
    # Listar
    elif opcao == '2':
        if not carros:
            print("Nenhum carro cadastrado.")
        else:
            print("\nLista de carros:")
            for carro in carros:
                print(f"ID: {carro['id']}, Modelo: {carro['modelo']}, Preço: R${carro['preco']:.2f}, Marca: {carro['marca']}")
 
    # Atualizar
    elif opcao == '3':
        if not carros:
            print("Nenhum carro cadastrado.")
        else:
            print("\nLista de carros:")
            for carro in carros:
                print(f"ID: {carro['id']}, Modelo: {carro['modelo']}, Preço: R${carro['preco']:.2f}, Marca: {carro['marca']}")
 
            id_busca = int(input("Digite o ID do carro para atualizar: "))
            encontrado = False
 
            for carro in carros:
                if carro['id'] == id_busca:
                    novo_modelo = input('Digite o novo modelo: ').title()
                    novo_preco = float(input('Digite o novo preço: '))
                    nova_marca = input('Digite a nova marca: ').title()
 
                    carro['modelo'] = novo_modelo
                    carro['preco'] = novo_preco
                    carro['marca'] = nova_marca
                    
                    with open(lista_carro, 'w') as arquivo:
                        for i in carros:
                            arquivo.write(f"{i['id']}|{i['modelo']}|{i['preco']}|{i['marca']}\n")

 
                    print('✅ Carro atualizado com sucesso!')
                    encontrado = True
                    break
 
            if not encontrado:
                print('❌ Carro não encontrado.')
 
    # Deletar
    elif opcao == '4':
        if not carros:
            print("Nenhum carro cadastrado.")
        else:
            print("\nLista de carros:")
            for carro in carros:
                print(f"ID: {carro['id']}, Modelo: {carro['modelo']}, Preço: R${carro['preco']:.2f}, Marca: {carro['marca']}")
 
            id_busca = int(input("Digite o ID do carro para deletar: "))
            encontrado = False
 
            for carro in carros:
                if carro['id'] == id_busca:
                    carros.remove(carro)
                    with open(lista_carro, 'w') as arquivo:
                        for i in carros:
                            arquivo.write(f"{i['id']}|{i['modelo']}|{i['preco']}|{i['marca']}\n")
                    print("✅ Carro deletado com sucesso!")
                    encontrado = True
                    break
 
            if not encontrado:
                print("❌ Carro não encontrado.")
 
    # Sair
    elif opcao == '0':
        print("Saindo do sistema...")
        time.sleep(2)
        total = 20
        for i in range(total + 1):
            porcentagem = (i / total) * 100
            barra = "✅" * i + "-" * (total - i)
            print(f'\r[{barra}] {porcentagem:.2f}%', end="")
            time.sleep(0.3)
        break