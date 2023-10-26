from criatura import Criatura

class Animal(Criatura):
    def __init__(self, nome, tipo, habitat, tamanho, velocidade):
        super().__init__(nome, tipo, habitat)
        self.tamanho = str(tamanho)
        self.velocidade = float(velocidade)
    
    def imprimir(self):
        super().imprimir()
        print(f"Tamanho: {self.tamanho}")
        print(f"Velocidade: {self.velocidade}")