"""
Sorted

OBS: Não confunda, apesar do nome, com função sort() que já estudamos em Listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS. O sorted() sempre retorna uma lista
"""

numeros = {6, 1, 8, 2}

print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True))


usuarios = [
    {"usename": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"usename": "carla", "tweets": ["Eu amo meu gato"]},
    {"usename": "jeff", "tweets": []},
    {"usename": "bob123", "tweets": [], "cor": "amarelo"},
    {"usename": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"usename": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["usename"]))
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]), reverse=True))

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Black in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))