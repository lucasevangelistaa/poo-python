class Aluno:
    def __init__(self,nome,num_matricula,idade,data_matricula,cpf,aluno_ativo):
        self.nome = nome
        self.num_matricula = num_matricula
        self.idade = idade
        self.data_matricula = data_matricula
        self.cpf = cpf
        self.aluno_ativo = aluno_ativo

    
    def aumentar_idade(self, nova_idade):
        self.idade += nova_idade
    

    def cancelar_matricula(self):
        if self.aluno_ativo == True:
            self.aluno_ativo = False
        else:
            self.aluno_ativo = True
    

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Número da Matrícula: {self.num_matricula}')
        print(f'Idade: {self.idade}')
        print(f'Data da Matrícula: {self.data_matricula}')
        print(f'CPF: {self.cpf}')
        print(f'Aluno ativo: {self.aluno_ativo}')