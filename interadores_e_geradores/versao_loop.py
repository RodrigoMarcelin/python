"""
criando loop em python
"""

for letra in [1, 2, 3, 4 ,5]:
    print(letra)

for letra in 'Geek Universite':
    print(letra)

def meu_loop(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_loop("Geek University")