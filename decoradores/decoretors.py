"""
Decorators 

- São funções
- Envolvem outras funções e aprimoram seu comportamentos;
- São exemplos de higher other functions
- tem sintaxe própria

/-------------------------------------------------------/
/        Function Decorator                             /
/-------------------------------------------------------/


"""

#Função simples:

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print("Tenha um ótimo dia!")
    return sendo

def saudacao():
    print("Seja bem-vindo(a) à Geek University")

def raiva():
    print("EU TE ODEIO!")

raiva_educada = seja_educado(raiva)

raiva_educada()

# decorator com açucar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print("Tenha um ótimo dia!")
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print("Meu nome é Pedro")