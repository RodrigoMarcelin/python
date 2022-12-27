"""
Herança multipla -> nada mais é do que a possibilidade de uma classe herdar de multiplas classes, fazendo com que a 
classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança multiplas pode ser feita de multiplas maneiras:
    - Por Multiderivação Direta;
    - Por multiderivação indireta;

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class MultiDerivada(Base1, Base2):
    pass

# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class MultiDerivada(Base2):
    pass

# OBS: Não importa de a derivação é direta ou intireta. A classe que realizar a herança herdará todos os atributos
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

#Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.nadar())
print(tux.andar())
print(tux.cumprimentar())


print(f'Tux é intância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é intância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é intância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é intância de object? {isinstance(tux, object)}')

