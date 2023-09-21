from pessoa import Pessoa

p = Pessoa()
p.definir_nome('lucas')
p.definir_idade(17)
p.definir_endereco('Rua: IFMA, Bairro: IF, N°: 00')
print(p.obter_nome())
print(p.obter_idade())
print(p.obter_endereco())
