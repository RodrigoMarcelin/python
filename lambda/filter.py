"""
Filter
Serve para filtrar dado de determinada função

"""
import statistics

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)

print(media)

res = filter(lambda x: x < media, dados)

print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(None, paises)
# res = filter(lambda x: len(x) > 0 , paises)

print(list(res))

usuarios = [
    {"usename": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"usename": "carla", "tweets": ["Eu amo meu gato"]},
    {"usename": "jeff", "tweets": []},
    {"usename": "bob123", "tweets": []},
    {"usename": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"usename": "gal", "tweets": []}
]

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
inativos = list(filter(lambda u: not u['tweets'], usuarios))

print(inativos)

nomes = ["Vanessa", 'Ana', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)