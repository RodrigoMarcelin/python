"""
Decorators com diferentes assinatura
"""

# def gritar(funcao):
#     def aumentar(nome):
#         return funcao(nome).upper()
#     return aumentar

# @gritar
# def saudacao(nome):
#     return f'Olá, eu sou o/a {nome}'

# print(saudacao('Angelina'))

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor'

print(ordenar("Bife", "fritas"))
print()
print(saudacao("Rodrigo"))

@gritar
def lol():
    return 'lol'

print(lol())

# Decorador com argumentos

def verificar_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa der {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verificar_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verificar_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2



# Testando

print(soma_dez(1, 20))
print(comida_favorita('sandwiche', 'churrasco'))