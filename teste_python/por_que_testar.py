"""
Testes Automatizados

TDD - Teste Driven Development (Desenvolvomento Geiadoa testes)

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
    - Então você escreve o código mínimo suficiente para passar no teste (ou seja executar com sucesso)
    - Então refatora o código para realizar a funcionalidade e testa novamente
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red
    - Green
    - Refactor
"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')

felix = Gato('Felix')

felix.miar()

print(felix.nome)
