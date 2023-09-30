class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_notas(self, notas):
        if len(notas) != 4:
            return 'ERRO! São necessárias 4 notas'
        for nota in notas:
            if type(nota) != float:
                return 'ERRO! As notas devem estar no tipo FLOAT.'
        self.notas = notas

    def obter_media(self):
        if len(self.notas) == 4:
            return sum(self.notas) / 4