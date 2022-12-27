"""
all() -> retorna True se todos os elementos do iteravel são verdadeiros ou se todos os iteraveis estão vazios
any() -> retorna True se qualquer um for verdadeiro, se o iteravel estiver vazio ele retorna false
"""

print(all([0, 1, 2, 3, 4]))
print(all([1, 2, 3, 4]))
print(all([]))
print(all(["Rodrigo"]))


nomes = ["Carlos", "Camila", "Carla", "Cassiano", "Cristina"]

print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra for letra in 'eio' if letra in 'aeiou']))


letras_validas = [1, 2, 4, 5]
lista = [8, 6, 7]

print(any([item for item in lista if item in letras_validas]))