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