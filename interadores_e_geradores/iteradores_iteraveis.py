"""
Iterator -> objeto que pode ser iterado
            objeto que retorna um dado, sendo um elemento por uma vez uma função next() é chamada

Interable -> Um objeto que retornará um Iterator quando a função iter() for chamada
"""

numeros = [1, 2, 3, 4, 5, 6] #iterable

it_numero = iter(numeros) # iterable

