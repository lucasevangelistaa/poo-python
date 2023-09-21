class UsuarioRedeSocial:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self._amigos = []
    
    def adicionar_amigo(self, usuario):
        self._amigos.append(usuario)
    
    def listar_amigos(self):
        return self._amigos
    
    def obter_nome(self):
        return self.__nome
    
    def obter_idade(self):
        return self.__idade
    
    def atualizar_nome(self, novo_nome):
        if  len(self.__nome) >= 3:
            self.__nome = novo_nome
        else:
            print('ERRO! Nome deve possuir pelo menos 3 caracteres.')
    
    def atualizar_idade(self, nova_idade):
        if self.__idade >= 0:
            self.__idade = nova_idade
        else:
            print('ERRO! Idade não pode ser negativa.')
    