"""
POO - Classes

Em POO, Classes nada mais são que modelos dos objetos do mundo real sendo representados computacionamente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter: 
- Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente
iriamos querer saber se a lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela e etc

- Métodos (função) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema. no caso da lâmpada, por exemplo, um comportamento comum
que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.


Em python para definir uma classe utilizamos a palavra reservada class.

Quando criamos uma classe utilizamos por convenção CamelCase

Classes são chamadas tbm de entidades

"""

class Lampada:
    pass

lamp = Lampada()

print(type(lamp))