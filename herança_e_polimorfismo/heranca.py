"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também de extender nossas classes

OBS: Com herança, a partir de uma classe existente, nós extendemos outras classes que passam a herdar atributos e métodos da classe herdado.


"""
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    

class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda




class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionario Matricula: {self.__matricula} Nome: {self._Pessoa__nome}'



cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())