class ItemVenda:
    
    def __init__(self, cli, prod, quant):
        self.cliente = cli
        self.produto = prod
        self.quantidade = quant
    
    def calcula_valor_total(self):
        return self.produto.valor * self.quantidade
    
    def imprimir(self):
        print(self.cliente.nome)
        print(self.produto.descricao)
        print(self.quantidade)
        total = self.calcula_valor_total()
        print(total)