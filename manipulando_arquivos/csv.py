
# """
# csv

# with open(r"C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Python\manipulando_arquivos\lutadores.csv") as arquivo:
#     dados = arquivo.read()
#     dados = dados.split(',')[2:]
#     print(dados)

# da para trabalhar mas não é o ideal
# """


# Reader

from csv import reader
from csv import DictReader

with open(r"C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Python\manipulando_arquivos\lutadores.csv", encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros')


with open(r"C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Python\manipulando_arquivos\lutadores.csv", encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']} centímetros")

