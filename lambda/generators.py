"""
Generators

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

não vimos Tuple Comprehension, porque elas se chamam Generators
"""
from sys import getsizeof


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res)
print(type(res))
print(getsizeof(res))

#Generator
res = (nome[0] == 'C' for nome in nomes)
print(res)
print(type(res))
print(getsizeof(res))

