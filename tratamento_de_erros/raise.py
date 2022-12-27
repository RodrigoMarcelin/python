"""
raise -> Lança exceção
"""


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("texto precisa der uma string")
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f"O texto {texto} será impresso na cor {cor}")

colore(4, 'verde')