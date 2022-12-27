"""
os.getcwd() -> pega o diretirio atual
os.isabs() -> verifica se esse diretorio é absoluto
os.chdir() -> aceita comandos de navegação
os.name -> mostra o sistema operacional 
os.uname() -> mostra o sistema operacional com detalhes se posix
sys.platform -> mostra o sistema operacional
os.path.join() -> acrecenta mais caminhos de pasta ao diretorio corrente
os.listdir() -> lista os arquivos do diretório atual
os.scandir() -> escaneia diretorio atual, exemplo:
    arquivos = list(os.scandir())
    arquivos[0].inode() -> ??
    arquivos[0].is_dir() -> verifica se é um dieretório
    arquivos[0].is_file() -> verifica se é um arquivo
    arquivos[0].is_symlink() -> verifica se é um link simbólico
    arquivos[0].name -> para saber o nome do arquivo
    arquivos[0].path -> caminho até o arquivo
    arquivos[0].stat() -> estatisticas sobre o arquivo
OBS: quando abrimos o scandir() devemos fechá-lo
"""
import os
print(os.name)
# print(os.uname())