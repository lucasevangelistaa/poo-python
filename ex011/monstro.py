from criatura import Criatura

class Monstro(Criatura):
    def __init__(self, nome, habitat, forca, resistencia, dano):
        super().__init__(nome, "Monstro", habitat, forca, resistencia, dano)
        self.forca = forca
        self.resistencia = resistencia
        self.dano = dano
    
    def imprimir(self):
        super().imprimir()
        print(f"Força: {self.forca}")
        print(f"Resistência: {self.resistencia}")
        print(f"Dano: {self.dano}")