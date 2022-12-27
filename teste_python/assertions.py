"""
Assertions (Afirmações/checagens/ Questionamentos)

utilizamos o 'assert' em uma expressão que queremos checar se é valida ou não.
se a expreção for verdadeira, retorna None e caso falsa levanta um erro do tipo AssertionError
"""


# def soma_numeros_positivos(a, b):
#     assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
#     return a + b


# ret = soma_numeros_positivos(-2, 4)
# print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita'
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return "Eu estou comendo {}".format(comida)

print(comer_fast_food('pizza'))
