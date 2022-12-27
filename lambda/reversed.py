"""
Reversed

OBS: Não confunda a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável

Sua função é inverter o interável

"""

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))

print(''.join(list(reversed('Rodrigo'))))
print('Rodrigo'[::-1])