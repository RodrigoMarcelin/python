"""
Leitura de Arquivos

open() -> Na forma mais simples de utilização nós passamos apenas um parametro de entrada 
que é o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então
"""

arquivo = open(r'C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Python\leitura de arquivos\texto.txt')
print(arquivo)

print(type(arquivo))

print(arquivo.read())

