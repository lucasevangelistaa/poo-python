from televisor import Televisor
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