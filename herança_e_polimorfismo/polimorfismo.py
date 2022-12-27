"""
Poli -> Muitas
Morfis -> Formas


"""

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implmentar este método')

    def comer(self):
        print(f"{self.__nome} está comendo...")

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

dog1 = Cachorro('Spyke')
cat1 = Gato('Tom')
mouse1 = Rato('Jerry')

dog1.comer()
dog1.falar()

cat1.comer()
cat1.falar()

mouse1.comer()
mouse1.falar()