"""
Funções de maior grandeza - Higher Order Functions - HOF


O que significa?

- Quandos uma linguagem de programação suporta HOF, indica que podemos ter funçoes que retornam outras funçoes como resuldo ou mesmo que podemos 
passar funções como argumetos para outras funlçoes, e até mesmo criar váriaveis do tipos de funções nos nossos programas

OBS: Na seção de funções, nós utilizamos isso.
"""
from random import choice

def soma(a, b):
    return a + b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 3, soma))

def cumprimentar(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimentar('Angelica'))