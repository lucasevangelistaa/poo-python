from aluno import Aluno

a1 = Aluno('Lucas',202010068, 17, '03/02/2020', 12345678912, True)
a1.exibir_dados()
a1.aumentar_idade(1)
a1.cancelar_matricula()
print('>'*40)
a1.exibir_dados()