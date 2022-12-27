"""
Seek e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo.
"""

arquivo = open(r'C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Python\leitura de arquivos\texto.txt')

print(arquivo.read())

arquivo.seek(22)

print(arquivo.read())

arquivo.seek(0)

print(arquivo.read(15))

arquivo.seek(0)

print(arquivo.readline())

arquivo.seek(0)

print(arquivo.readlines())
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)