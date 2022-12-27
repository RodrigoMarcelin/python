"""
bloco with
Forma pythonica de se trabalhar com arquivos

1 - Abrimos o arquivo
2 - Manipulamos o arquivo
3 - Fechamos o arquivo

O block with é utilizado para criar um contexto de trabalho onde os recursos utilizados sção  fechados após o bloco with

"""

with open(r'C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Python\leitura de arquivos\texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)