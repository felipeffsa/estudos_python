class Animal:
    def __init__(self,nome,familia,cor):
        self.nome = nome
        self.familia = familia
        self.cor = cor
    
    
    def correr(self):
        return f"O animal {self.nome} está correndo"
    
    
    def comer(self):
        print(f"O animal {self.nome} está comendo")





cachorro = Animal("cachorrinho","canideo","preto")

print(cachorro.correr())

# Aqui é mostrado como a gente pode fazer uma herança de classes no python
class Capivara(Animal):
    def nadar(self):
        print("A capivara está nadando")
# Aqui é mostrado como a gente pode modificar um metodo da classe pai
    def correr(self):
        return super().correr() + " porque ela é uma capivara"


capivarinha = Capivara("capivarinha","capivaridea","marrom")

print(capivarinha.correr())



