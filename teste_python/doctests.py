"""
Doctests

python -m doctest -v nome_do_modulo.py

def soma(a, b):
    '''
    # soma do numeros a e b
    # >>> soma(1, 2)
    # 3
    '''
    return a + b

print(soma(3, 4))
"""

def duplicar(valores):
    """duplicar os valores em uma lista
    
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]

