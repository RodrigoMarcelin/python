"""
Len, Abs, Sum, Round

len() -> retorna o tamanhos do interavel
abs() -> retorna o numero inteiro sem sinal, ou o numero real
sum() -> recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial defaut = 0
round() -> serve para arredondar numeros reais, ele fica default inteiro ou podemos colocar a quantidade de casas decimais

"""

print(len("Rodrigo"))
print(abs(5))
print(abs(-5))
print(abs(5.147))

print(sum([1, 2 ,3 , 4, 5]))
print(sum([1, 2 ,3 , 4, 5], 5))
print(sum([1, 2 ,3 , 4, 5], -5))
print(sum([3.145, 5.678]))
print(sum((1, 2 ,3 , 4, 5)))
print(sum({1, 2 ,3 , 4, 5}))
print(sum({'a': 1, 'b': 2 ,'c': 3 , 'd': 4, 'e': 5}.values()))

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2121212121, 2))
print(round(1.2199999999, 2))


