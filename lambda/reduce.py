"""
REDUCE
A partir da versão 3x a função reduce não é mais integrada
Para utilizar esta função deve importar a functools
"""
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y

res = reduce(multi, dados)

print(res)

