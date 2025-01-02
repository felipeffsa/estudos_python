# Criando a sua propria exception


class MinhaExcecaoError(Exception):
    pass

try:
    erro = True
    # ...
    if erro:
        raise MinhaExcecaoError("Ocorreu um erro!")

except MinhaExcecaoError as mensagem:
    print(mensagem)
