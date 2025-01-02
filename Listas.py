frutas = ["uva","maça","manga","melao","maracujá"]
# list_comprehension - como usar
frutas_numeradas = [fruta for fruta in frutas]

# como usar o enumerate
for indice, fruta in enumerate(frutas):
    print(f"Essa é a fruta {fruta.title()} e esse e o seu indice {indice}")

# Como usar o enumerate com o list_comprehension
frutas_enumeradas = [(indice,fruta) for indice,fruta in enumerate(frutas)]

for indice,fruta in frutas_enumeradas:
    print(f"Esse é o indice {indice} e essa é a fruta {fruta.title()}")


#Explicando o list comprehension
#Lista_explica = [item for item in itens]