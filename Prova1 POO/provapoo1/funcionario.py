class Funcionario:
    def __init__(self, nome, departamento, salario, data_entrada, rg, ativo):
        self.nome = nome
        self.departamento = departamento
        self.salario = salario
        self.data_entrada = data_entrada
        self.rg = rg
        self.ativo = ativo
        
    def bonifica(self, valor):
        self.salario += valor
        
    def demite(self):
        if self.ativo == True:
            self.ativo = False
        
    def mostrar(self):
        print(f'Nome: {self.nome}')
        print(f'Departamento: {self.departamento}')
        print(f'Salário: {self.salario}')
        print(f'Data de entrada: {self.data_entrada}')
        print(f'RG: {self.rg}')
        print(f'Ativo: {self.ativo}')