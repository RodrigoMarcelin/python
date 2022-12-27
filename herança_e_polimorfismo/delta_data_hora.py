import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2023, 3, 3, 0)

tempo_do_evento = aniversario - data_hoje

print(type(tempo_do_evento))

print(repr(tempo_do_evento))

print(tempo_do_evento)

compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)
vencimento_boleto = compra + regra_boleto

print(compra)
print(regra_boleto)
print(vencimento_boleto)