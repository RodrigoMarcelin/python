"""
List Comperhension
Nós podemos adicionar estruturas condicionais lógicas às nissas List Comperhension
"""

#Exemplos

numeros = [1, 2, 3, 4, 5, 6, 7]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

pares_1 = [numero for numero in numeros if not numero % 2]
impares_1 = [numero for numero in numeros if numero % 2 ]

print(pares_1)
print(impares_1)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)