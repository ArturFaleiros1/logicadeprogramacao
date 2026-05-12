
lista_notas = []

print (20*"-", "Sistema de Notas ",20*"-")
while True:
    nota = int(input("Digite a nota que deseja: "))
    lista_notas.append(nota)
    op = input("Deseja adicionar mais nota? s - sim e n - não ")
    if op != "s":
       break

media = sum(lista_notas)/len(lista_notas)

print(f"Sua média final é {media:.2f}")
if media >= 7:
    print("Você esta aprovado!")

elif media >=5:
    print("Você está de recuperação")

else:
    print("Você está reprovado!")
