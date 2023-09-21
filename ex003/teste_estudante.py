from estudante import Estudante
from turma import Turma

#Teste Turma
turma = Turma("2° TI VESPERTINO")

#Adicionar dois estudantes a turma
turma.adicionar_estudante(2020, {"nome": "Lucas", "notas": {1: 5.3, 2: 8.0, 3: 8.0, 4: 6.0}})

turma.adicionar_estudante(2019, {"nome": "João", "notas": {1: 9.0, 2: 8.0, 3: 7.0, 4: 5.0}})


dados_lucas = turma.obter_dados_estudantes(2020)
print(dados_lucas)

print('_'*60)

dados_joao = turma.obter_dados_estudantes(2019)
print(dados_joao)

print('='*30)
media_prova_1 = turma.obter_media_prova(1)
print(f' A média das provas foi {media_prova_1}')