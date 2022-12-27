import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


    def comer(self):
        print(f'{self.__nome} está comendo')



class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo')


felix = Gato('Felix')
pluto = Cachorro('Pluto')


with open(r'C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Python\manipulando_arquivos\animais.pikle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)

with open(r'C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Python\manipulando_arquivos\animais.pikle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')
    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')