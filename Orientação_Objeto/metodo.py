"""
- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instancia e Métodos de Classes.

#Métodos de instacia

# O metodo __init__ é um metodo construtor e sua função é construir o objeto a partir da classe
"""
from passlib.hash import pbkdf2_sha256 as crypt
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crypt.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if crypt.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(50))

user1 = Usuario('Rodrigo', 'Marcelino', "rodrigoamorimdhy@gmail.com", '@Mtpe3202')

print(user1.nome_completo())

print(user1._Usuario__senha)

