"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever o arquivo

StringIO -> Utilizado para ler e criar arquivos em memória

"""

from io import StringIO

mensagem = 'Este é apenas uma string normal'

arquivo = StringIO(mensagem)

print(arquivo.read())

arquivo.write('\n')
arquivo.write('Outro texto')
arquivo.seek(0)

print(arquivo.read())