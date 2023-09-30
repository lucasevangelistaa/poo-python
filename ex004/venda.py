class Venda:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items_venda = []
    
    def adicionar_item(self, item):
        self.items_venda.append(item)
    
    def caucula_valor_total(self):
        total = 0
        for item in self.items_venda:
            total += item.calcula_valor_total()
        
        return total