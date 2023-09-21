class Moto:

    def __init__(self, marca, modelo, cor, marcha=0,menor_marcha=0,maior_marcha=5, ligada=False):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.menor_marcha = menor_marcha
        self.maior_marcha = maior_marcha
        self.ligada = ligada
        
        
    def ligar(self):
        if not self.ligada:
            self.ligada = True
            print('MOTO LIGADA')
        else:
            print('MOTO JÁ ESTÁ LIGADA!')
    
    def desligar(self):
        if self.ligada == True:
            self.ligada = False
            print('MOTO DESLIGADA')
        else:
            print('MOTO JÁ ESTÁ DESLIGA!')
        
        
    def marcha_cima(self):
        if self.marcha < self.maior_marcha:
            self.marcha += 1
            print(f'Subindo para marcha {self.marcha}')
        else:
            print('Não é Possível subir mais marchas!')
            
            
    def marcha_baixo(self):
        if self.marcha > self.menor_marcha:
            self.marcha-= 1
            print(f'Descendo para a marcha {self.marcha}')
        else:
            print('Não é Possível descer mais marchas!')
            
    
    def imprimir(self):
        print('>'*40)
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Marcha: {self.marcha_extenso()}')
        print(f'Menor Marcha: {self.menor_marcha}')
        print(f'Maior Marcha: {self.maior_marcha}')
        if self.ligada:
            print(f'Ligada: SIM')
        else:
            print(f'Ligada: NÃO')
        print('<'*40)
        
        
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