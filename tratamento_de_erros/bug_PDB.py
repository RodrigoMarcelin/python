"""
Debuggando com PDB

PDB -> Python Debugger
"""

#COMANDOS BASICOS PDB:
"""
l (listar onde estamos no código)
n (próxima linha)
p (imprime variável)
c (continua a execução - finaliza o debugger)
"""
# import pdb


def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        # pdb.set_trace()
        breakpoint()# para versões acima da 3.7
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um probleminha {err}'

print(dividir(4, 7))
# OBS: utilizar o Python para debugger é uma pratica ruim

