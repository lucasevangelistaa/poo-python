class ContaBancaria:
    def __init__(self,titular, saldo, senha):
        self.__titular = titular
        self.__saldo = 0
        self.__senha = senha
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor_adicional):
        self.__saldo = valor_adicional
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("ERRO!")
    
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('ERRO!')
    
    def mudar_senha(self, senha_atual, nova_senha):
        if self.__senha == senha_atual:
            self.__senha = nova_senha
            print(f'Senha alterada com sucesso!')
        
        else:
            print('ERRO!')