class Calculadora:
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def soma(self):
        som = self.n1 + self.n2
        return som
    
    def multiplicacao(self):
        mult = self.n1 * self.n2
        return mult
    
    def divisao(self):
        divi = self.n1 / self.n2
        return divi
    
    def subtracao(self):
        subtra = self.n1 - self.n2
        return subtra
    
    def potenciacao(self):
        poten = self.n1 ** self.n2
        return poten
    
    def radiacao(self):
        radia = self.n1 ** (1/self.n2)
        return radia