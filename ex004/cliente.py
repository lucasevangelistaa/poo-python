class Cliente:
    
    def __init__(self, cod, nome):
        self.codigo = cod
        self.nome = nome
    
    def imprimir(self):
        print(self.codigo)
        print(self.nome)