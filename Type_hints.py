# Como utilizar o type hints nas classes do python
# A tipagem ou type hints é utilizado para mostrar o que se espera do argumento
def cadastro(nome:str, idade:int) -> str:
    return f"Esse é o seu nome {nome} e essa é sua idade {idade}"


pessoa_01 = cadastro("felipe",26)

print(pessoa_01)

