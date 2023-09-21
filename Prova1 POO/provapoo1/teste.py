from funcionario import Funcionario

f1 = Funcionario('Lucas', 'Gerencia', 1200, '01/01/2000', 123456789, True)

f1.mostrar()
print('_'*15)
f1.bonifica(300)
f1.demite()
f1.mostrar()