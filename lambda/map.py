"""
Map

Com map, fazemos mapeamento de valores para função
"""
import math

def area(r):
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5.3]

areas = []
for r in raios:
    areas.append(area(r))


print(areas)

areas_map = map(area, raios)
print(list(areas_map))
print(list(map(lambda r: math.pi * (r ** 2), raios)))


cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

print(cidades)

lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))

# lista = lambda dado: FeateureClassGenerator()