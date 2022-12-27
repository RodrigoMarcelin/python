"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension

[dado for dado in irterável]

"""

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

res_2 = [numero / 2 for numero in numeros]
print(res_2)

def funcao(valor):
    return valor * valor

res_3 = [funcao(numero) for numero in numeros]
print(res_3)

"""
List Comprehension vs Loop
"""
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

numeros_dobrados_c = [num * 2 for num in numeros ]
print(numeros_dobrados_c)

