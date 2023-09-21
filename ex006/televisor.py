class Televisor:
    def __init__(self, ligado, canal_atual, volume):
        self.__ligado = ligado
        self._canal_atual = canal_atual
        self._volume = volume
    
    def ligar(self):
        self.__ligado = True
    
    def desligar(self):
        self.__ligado =  False
    
    def mudar_canal(self, numero_canal):
        self._canal_atual = numero_canal
    
    def aumentar_volume(self):
        self._volume += 1

    def diminuir_volume(self):
        self._volume -= 1
    
    def exibir_status(self):
        print(f'Ligado: {self.__ligado}')
        print(f'Canal atual: {self._canal_atual}')
        print(f'Volume: {self._volume}')

class ControleRemoto:
    def __init__(self):
        self.__televisor = None
    
    def associar_televisor(self, televisor):
        if isinstance(televisor, Televisor):
            self.__televisor = televisor
        else:
            print("Erro: O objeto associado ao controle remoto deve ser uma instância da classe Televisor.")
    
    def ligar_televisor(self):
        if self.__televisor is not None:
            self.__televisor.ligar()
        else:
            print("Erro: Nenhum televisor associado ao controle remoto.")
    
    def desligar_televisor(self):
        if self.__televisor is not None:
            self.__televisor.desligar()
        else:
            print("Erro: Nenhum televisor associado ao controle remoto.")
    
    def mudar_canal(self, numero_canal):
        if self.__televisor is not None:
            self.__televisor.mudar_canal(numero_canal)
    
    def aumentar_volume(self):
        if self.__televisor is not None:
            self.__televisor.aumentar_volume()

    def diminuir_volume(self):
        if self.__televisor is not None:
            self.__televisor.diminuir_volume()
    
    def exibir_status_televisor(self):
        if self.__televisor is not None:
            self.__televisor.exibir_status()
    
    