"""
max() -> retorna o maior valor em um iterável ou o maior de dois ou mais elemento.
min() -> retorna o menor valor em um iterável ou o menor de dois ou mais elemento.
"""

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'f': 34, 'g': 129}
print(max(dicionario))
print(max(dicionario.values()))

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Black in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou'])["titulo"])
print(min(musicas, key=lambda musica: musica['tocou'])["titulo"])