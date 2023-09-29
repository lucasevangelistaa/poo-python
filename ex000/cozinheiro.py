class Cozinheiro:
    def __init__(self,trigo,ovos,manteiga,leite,fermento):
        self.trigo = trigo
        self.ovos = ovos
        self.manteiga = manteiga
        self.leite = leite
        self.fermento = fermento

    def misturar_ingredientes(self):
        print('Misturando os ingredientes...')

    def dascansar_massa(self,tempo):
        print(f'Deixando a massa descansar por {tempo} minutos')
    
    def levar_ao_forno(self,tempo):
        print(f'Assando o bolo por {tempo} minutos')

    def resfriar(self, tempo):
        print(f'Resfriando o bolo por {tempo} minutos')

    def fazer_bolo(self):
        self.misturar_ingredientes()
        self.descansar_massa()
        self.levar_ao_forno()
        self.resfriar()