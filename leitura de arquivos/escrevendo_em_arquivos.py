"""
Escrevendo em arquivos

Ao abrir um arquivo para leitura não poderemos escrever nele e vice e versa
a função write não recebe numero
"""

with open(r'C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Python\leitura de arquivos\novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha')