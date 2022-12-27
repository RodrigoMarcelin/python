"""
Preservando metadatas com wraps

Metadados -> São dados instrisecos em arquivos.

wraps -> São funções que envolvem elementos com diversas dinalidades
"""

# Problema
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma funçãp (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


print(soma(2, 3))

print(soma.__name__)
print(soma.__doc__)