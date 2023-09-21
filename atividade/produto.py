class Produto:
    
    def __init__(self, cod, desc, val):
        self.codigo = cod
        self.descricao = desc
        self.valor = val
    
    def imprimir(self):
        print(self.codigo)
        print(self.descricao)
        print(self.valor)