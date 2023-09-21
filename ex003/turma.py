from estudante import Estudante
class Turma:
    def __init__(self,nome):
        self.nome = nome
        self.estudantes = {}
    
    
    def adicionar_estudante(self, matricula, dados_estudante):
        if matricula in self.estudantes:
            return 'ERRO! Um estudante já está com essa matrícula'
        else:
            self.estudantes[matricula] = dados_estudante
                
    
    def obter_dados_estudantes(self, matricula):
        if matricula in self.estudantes:
            return self.estudantes[matricula]
        else:
            return 'ERRO! Não tem estudante com essa matrícula.'
            
    
    def obter_media_prova(self, num_prova):
        notas = []
        for estudante in self.estudantes.values():
            if num_prova in estudante["notas"]:
                notas.append(estudante["notas"][num_prova])
        if notas:
            return sum(notas) / len(notas)
        else:
            return 'ERRO! Não tem notas registradas pra essa prova.'