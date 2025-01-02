#Aqui aprenderemos como utilizar o with no python
# É utilizado para trabalhar com coisas que precise de uma inicialização e finalização

with open("test.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


# Sem o with, o usuario deve lembrar de fechar o arquivo
arquivo = open("arquivo.txt", "r")
try:
    conteudo = arquivo.read()
    print(conteudo)
finally:
    arquivo.close()