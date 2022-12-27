"""
Zip

zip() -> Cria m iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares
"""

lista = [1, 2, 3, 4, 5]
lista_2 =[6, 7, 8, 9, 10]

zip1 = zip(lista, lista_2)

print(zip1)
print(type(zip1))

print(list(zip1))
zip1 = zip(lista, lista_2)
print(tuple(zip1))
zip1 = zip(lista, lista_2)
print(set(zip1))
zip1 = zip(lista, lista_2)
print(dict(zip1))

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))