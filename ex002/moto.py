class Moto:
    def __init__(self, marca, modelo, cor, marcha, menor_marcha, maior_marcha, ligada=False):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.menor_marcha = menor_marcha
        self.maior_marcha = maior_marcha
        self.ligada = ligada
        
    def ligar(self):
        if self.ligada == False:
            self.ligada = True
    
    def desligar(self):
        if self.ligada == True:
            self.ligada = False

    def marcha_acima(self):
        if self.marcha < self.maior_marcha:
            self.marcha += 1
            
    def marcha_abaixo(self):
        if self.marcha > self.menor_marcha:
            self.marcha -= 1
            
    def imprimir(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Marcha: {self.marcha_extenso()}')
        print(f'Menor Marcha: {self.menor_marcha}')
        print(f'Maior Marcha: {self.maior_marcha}')
        print(f'Ligada: {self.ligada}')
              
    def marcha_extenso(self):
        if self.marcha == 0:
            return 'NEUTRO'
        elif self.marcha == 1:
            return 'PRIMEIRA'
        elif self.marcha == 2:
            return 'SEGUNDA'
        elif self.marcha == 3:
            return 'TERCEIRA'
        elif self.marcha == 4:
            return 'QUARTA'
        elif self.marcha == 5:
            return 'QUINTA'
        else:
            return 'ERRO NA TROCA DE MARCHA!!'