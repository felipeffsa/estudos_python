#Aqui estudaremos os loops em python


# Laço while
flag = True
lista_nomes = []

while flag:
    digite = input("Digite seu nome aqui: ")
    lista_nomes.append(digite)
    print("Deseja adicionar mais pessoas ?")
    print("Digite 's' para sim e 'n' para não")
    continuar = input("Digite aqui: ")
    if continuar.lower() == "n":
        print("Voce optou por parar o programa")
        flag = False
    else:
        pass


print(lista_nomes)


# Laço for

frutas = ["uva","maça","banana","morango"]

for fruta in frutas:
    print(fruta)

