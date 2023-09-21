from produto import Produto

p1 = Produto('Arroz', 12345, 2, '01/01/2001', 54321, False)


p1.imprimir_dados()
p1.aumentar_quantidade(2)
p1.vender()
print('_'*40)
p1.imprimir_dados()