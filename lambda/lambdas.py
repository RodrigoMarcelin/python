"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou Simplesmente Lambdas, são funções sem nome, ou seja, função anonima

"""

# Função

def funcao(x):
    return 3 * x + 1


print(funcao(4))


# Expressão Lambda

lamb = lambda x: 3 * x + 1

print(lamb(4))

# Podemos ter expreções lambdas com mltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('rodrigo', 'amorim    '))

# Em Funções python podemos ter nenhuma ou varias entradas

amar = lambda: 'Como não amar Python ?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1/ x + 1/ y + 1/ z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#

lista_autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Oson Scott Card',
                 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

lista_autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(lista_autores)

"""
Função quadratica
f(x) = a * x **2 + b * x + c
"""

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))