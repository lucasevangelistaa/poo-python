class Produto:
    def __init__(self, nome, num_cadastro, quantidade, data_validade, codigo, vendido):
        self.nome = nome
        self.num_cadastro = num_cadastro
        self.quantidade = quantidade
        self.data_validade = data_validade
        self.codigo = codigo
        self.vendido = vendido
       
    def aumentar_quantidade(self, aumento_qtd):
        self.quantidade += aumento_qtd
    
    def vender(self):
        if self.vendido == True:
            self.vendido = False
        else:
            self.vendido = True
    
    def imprimir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Número do Cadastro: {self.num_cadastro}')
        print(f'Quantidade: {self.quantidade}')
        print(f'Data de validade: {self.data_validade}')
        print(f'Código: {self.codigo}')
        print(f'Vendido: {self.vendido}')