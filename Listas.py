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

# Como utilizar um if no list comprehension
# Devemos lembrar que o if deve sempre ficar no final
numeros = [numero for numero in range(1,11) if numero >3]

print(numeros)

# Como utilizar um if e else no list comprehension
# Caso o else esteja junto do if, é necessario que os dois venham primeiro
numeros = [numero*2 if numero>3 else "nada" for numero in range(1,11)]

print(numeros)