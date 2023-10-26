from monstro import Monstro
from animal import Animal

monstro1 = Monstro("Ogro", "Monstro", "Floresta", 10, 8, 12)
animal1 = Animal("Leão", "Animal", "Savana", "Grande", 50.0)

monstro1.imprimir()

animal1.imprimir()

monstro1.atacar(animal1)
animal1.defender(monstro1)

if isinstance(monstro1, Monstro):
    print(f"{monstro1.nome} é um Monstro")
if isinstance(animal1, Animal):
    print(f"{animal1.nome} é um Animal")