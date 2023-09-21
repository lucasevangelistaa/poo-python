class Veiculo:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def get_cor(self):
        return self.cor
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, numero_de_portas):
        super().__init__(marca, modelo, cor)
        self.numero_de_portas = numero_de_portas
    
    def get_numero_de_portas(self):
        return self.numero_de_portas

class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, cor, cilindrada, tipo_de_motor):
        super().__init__(marca, modelo, cor)
        self.cilindrada = cilindrada
        self.tipo_de_motor = tipo_de_motor
    
    def get_cilindrada(self):
        return self.cilindrada
    
    def get_tipo_de_motor(self):
        return self.tipo_de_motor