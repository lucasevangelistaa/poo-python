class Venda:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens_venda = []
    
    def adicionar_item(self, item):
        self.itens_venda.append(item)
    
    def caucula_valor_total(self):
        total = 0
        for item in self.itens_venda:
            total += item.calcula_valor_total()
        
        return total