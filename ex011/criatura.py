class Criatura:
    def __init__(self, nome, tipo, habitat, forca, resistencia, dano):
        self.nome = nome
        self.tipo = tipo
        self.habitat = habitat
        self.forca = forca
        self.resistencia = resistencia
        self.dano = dano
        self.vida = 100

    def atacar(self, inimigo):
        dano_causado = self.forca + self.dano
        inimigo.defender(dano_causado)

    def defender(self, dano):
        dano_recebido = max(dano - self.resistencia, 0)
        self.vida -= dano_recebido

    def imprimir(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Habitat: {self.habitat}")
        print(f"Vida: {self.vida}")