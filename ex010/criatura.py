class Criatura:
    def __init__(self, nome, tipo, habitat):
        self.nome = nome
        self.tipo = tipo
        self.habitat = habitat
    
    def get_forca_total(self):
        return 0
    
    def get_defesa_total(self):
        return 0
    
    def imprimir(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Habitat: {self.habitat}")
    
    def atacar(self, monstro_alvo):
        print(f"{self.nome} atacou {monstro_alvo.nome}")

    def defender(self, ataque):
        print(f"{self.nome} defendeu-se do ataque")
        return ataque

    def get_tipo_completo(self):
        return f"{self.tipo} - {self.habitat}"