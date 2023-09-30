from produto import Produto
from item_venda import ItemVenda
from cliente import Cliente
from venda import Venda

pacote_sal = Produto(1, 'pacote de sal', 2.5)
iphone = Produto(2, 'iPhone 14 Pro Max', 8000.0)
ovo_pascoa = Produto(3, 'Ovo de Páscoa Cacau Show', 80)

lucas = Cliente(1, 'Lucas')

item_venda1 = ItemVenda(lucas, pacote_sal, 3)
item_venda2 = ItemVenda(lucas, iphone, 2)

venda = Venda(lucas)
venda.adicionar_item(item_venda1)
venda.adicionar_item(item_venda2)
total = venda.caucula_valor_total()
print(total)