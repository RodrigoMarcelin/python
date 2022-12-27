import json

ret = json.dumps(['produtos', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Angorá')