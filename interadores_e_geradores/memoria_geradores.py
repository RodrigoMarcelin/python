"""
Teste de memoria com generators

"""

# def fib_lista(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, a + b
#     return nums

# # Teste
# for n in fib_lista(10000):
#     print(n)

# Geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

for n in fib_gen(10000):
    print(n)