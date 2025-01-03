class Pai:
    def __init__(self):
        print("Eu sou o pai")



class Filho(Pai):
    def __init__(self):
        super().__init__()
        print("Eu sou o filho")


class Neto(Filho):
    def __init__(self):
        super().__init__()
        print("Eu sou o neto")



neto = Neto()