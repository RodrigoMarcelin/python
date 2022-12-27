"""
Geradores (Generators) são Iteradores (Interators)
OBS: o cortrário não é verdadeiro

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com expreções geradoras

--------------------------------------------------------------------------------------------------------
/ Funções                                          / Generation Functions                              /
--------------------------------------------------------------------------------------------------------
/ utilizam return                                  / utilizam yield                                    /
--------------------------------------------------------------------------------------------------------
/ retorna uma vez                                  / podem utilizar yield múltiplas vezes              /
--------------------------------------------------------------------------------------------------------
/ quando executada, retorna um valor               / quanto executada, retorna um generator            /
--------------------------------------------------------------------------------------------------------
"""

# Exemplo de generation function

def conta_ate(valor_maximo) :
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

#OBS: uma generator function não é um generator ela gera um generator.

gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


gen = conta_ate(5)
print(list(gen))


