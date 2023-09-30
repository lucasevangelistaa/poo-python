from estudante import Estudante
from turma import Turma

# Criar estudantes
e1 = Estudante('Caio')
e2 = Estudante('Godofredo')
e3 = Estudante('Creuza')

# Adicionar notas aos estudantes
e1.adicionar_notas([8.0, 8.0, 5.0, 8.0])
e2.adicionar_notas([8.0, 7.0, 8.0, 7.0])
e3.adicionar_notas([8.0, 4.0, 9.0, 8.0])

# Criar uma turma
turma = Turma('Turma A')

# Adicionar estudantes à turma
turma.adicionar_estudante(123, e1)
turma.adicionar_estudante(456, e2)
turma.adicionar_estudante(789, e3)

# Calcular a média da prova 2 na turma
print(turma.obter_media_prova(4))