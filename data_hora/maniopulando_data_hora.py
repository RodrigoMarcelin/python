"""
Manipulando Data e hora
"""

import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print(datetime.datetime.now())

inicio = datetime.datetime.now()

print(inicio)

replace_inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(replace_inicio)

evento = datetime.datetime(2019, 1, 1, 0)

print(evento)

