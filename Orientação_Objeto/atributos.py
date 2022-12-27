"""
Atributos representam as caracteristicas de um objeto

Em python dividimos atritos em 3 grupos:
    -Atributos de Instância
    -Atributo de Classe
    -Atributos Dinâmicos

# Atributos de instância: São atributos declarados dentro do método construtor.

comparação Java e Python

JAVA:
public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligado = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

    public int getVoltagem(){
        return this.voltagem;
    }
}

EM python, por conveção, ficou estabelecido que, todo atributo de uma classe é publico.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se 
__ duplo underscore no inicio da variavel

isso é conhecido como name Mangling

"""

class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligado = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor
    
    @property
    def ligado(self):
        return self.__ligado


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador - self.id
    

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

p1 = Produto('Playstation 4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

p2.peso = '5kg'

print(p1.__dict__)
print(p2.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)