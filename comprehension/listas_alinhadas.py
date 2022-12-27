"""
Listas Aninhadas

-Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);
"""
# Exemplo

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(valor) for valor in lista] for lista in listas]

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)