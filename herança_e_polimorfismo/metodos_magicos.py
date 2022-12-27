"""
Metodos magicos

Métodos magicos, são todos os métodos que utilizam dunder.

init -> serve para construtor
repr -> descreve a classe
str -> também descreve a classe porém tem preferencia
len -> especifica qual atributo
del -> da para imprimir um msg parta a classe excluida

"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


    def __repr__(self):
        return self.titulo

    def __str__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)


print(livro1)
print(livro2)
print(len(livro1))