"""
Dictionary Comprehension

pense no seguinte:

Se quisermos criar uma tupla:
()

Se quisermos criar uma lista:
[]

Se quisermos criar um set:
{}

se quisermos montar um dicionario:
{key: valor}
"""

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}


print(quadrado)


numero = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numero}

print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}

print(mistura)

res = {num:('par' if num % 2 == 0 else 'impar') for num in numero}

print(res)