class Pessoa:
    def __init__(self):
        self.__nome = ''
        self.__idade = 0
        self.__endereco = ''
    
    def definir_nome(self, nome):
        self.__nome = nome
        
    def obter_nome(self):
        return self.__nome
    
    def definir_idade(self, idade):
        if idade == type(int) or idade > 0:
            self.__idade = idade
        else:
            print('O valor não é inteiro')
            
    
    def obter_idade(self):
        return self.__idade
    
    def definir_endereco(self, ender):
        self.__endereco = ender
    
    def obter_endereco(self):
        return self.__endereco