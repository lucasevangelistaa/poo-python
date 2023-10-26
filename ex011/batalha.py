import random
from criatura import Criatura

class Batalha:
    def __init__(self):
        # Lista onde serão armazenadas as criaturas
        self.criaturas = []

    def criar_criatura(self, nome, tipo, habitat, forca, resistencia, dano):
        # Instancia da Class Criatura
        criatura = Criatura(nome, tipo, habitat, forca, resistencia, dano)
        # Adicionando as criaturas na Lista
        self.criaturas.append(criatura)

    def iniciar_batalha(self):
        # Verificando se tem 2 Criaturas para a Batalhar
        if len(self.criaturas) < 2:
            print("É necessário pelo menos duas criaturas para a batalha.")
            return

        # Escolha aleatória do cenário
        cenarios = ["Floresta", "Montanha", "Caverna", "Deserto", "Tempestade"]
        cenario = random.choice(cenarios)
        print(f"\n** Iniciando Batalha no cenário: {cenario} **")

        # Vantagem do cenário
        for criatura in self.criaturas:
            if criatura.habitat == cenario:
                criatura.forca += 20
                print(f"{criatura.nome} ganhou uma vantagem de força no cenário {cenario}!")

        jogador1, jogador2 = random.sample(self.criaturas, 2)

        print(f"\n** {jogador1.nome} contra {jogador2.nome} **")

        # Loop da Batalha
        while jogador1.vida > 0 and jogador2.vida > 0:
            self.realizar_rodada(jogador1, jogador2)
            if jogador2.vida <= 0:
                print(f"\n{jogador1.nome} venceu!")
            else:
                self.realizar_rodada(jogador2, jogador1)
                if jogador1.vida <= 0:
                    print(f"\n{jogador2.nome} venceu!")

    def realizar_rodada(self, atacante, defensor):
        print(f"\n** Turno de {atacante.nome} **")
        print(f"{atacante.nome} - Vida: {atacante.vida}")
        print(f"{defensor.nome} - Vida: {defensor.vida}")
        print("Escolha uma ação:")
        print("1. Atacar")
        print("2. Defender")
        acao = input("Ação (1/2): ")
        if acao == "1":
            atacante.atacar(defensor)
            print(f"{atacante.nome} ataca {defensor.nome} e causa {atacante.forca + atacante.dano} de dano!")
        elif acao == "2":
            print(f"{defensor.nome} defende!")


print("=="*50)
print("Bem-vindo ao jogo de batalhas entre criaturas mitológicas!")
print("=="*50)

# Chamando a Class Batalha
jogo = Batalha()

# Laço de repetição para o Jogador 1 Jogador 2
for i in range(2):
    print("__"*50)
    nome = input(f"Jogador {i+1}, crie sua criatura:\n>Nome: ")
    tipo = input(">Tipo: ")
    habitat = input(">Habitat: ")
    forca = int(input(">Força: "))
    resistencia = int(input(">Resistência: "))
    dano = int(input(">Dano: "))
    jogo.criar_criatura(nome, tipo, habitat, forca, resistencia, dano)
    print("__"*50)
print("\n** Iniciando Batalha **")
jogo.iniciar_batalha()