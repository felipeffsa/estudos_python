from inicial import somar
# O método mágico 'name' serve para dizer o nome do arquivo que está sendo executado
# se o arquivo está sendo executado, o nome dele é 'main'
# caso ele nao é o arquivo que está sendo executado o nome dele será o nome do arquivo sem o py no final
print(__name__)

# O método mágico 'str' serve para chamar a a função __str__ quando a instancia da classe for inicializada
# Ela é utilizada dentro de uma classe
def __str__():
    return "algo"

# Outro método utilizado é o __eq__, ele basicamente é um metodo de comparação (igualdade)
# Se a idade de uma pessoa for igual a outro, por exemplo
# Para utilizar ele, criamos uma classe, e dentro dele botamos o self e o outro(instacia da classe)
# logo iremos comparar duas instancias
class Humano:
    def __init__(self,nome,idade,cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor
    
    def __eq__(self,outro): # Método __eq__
        return self.idade == outro.idade



pessoa_01 = Humano("felipe",27,"branco")
pessoa_02 = Humano("vitoria",26,"branco")

print(pessoa_01 == pessoa_02)
