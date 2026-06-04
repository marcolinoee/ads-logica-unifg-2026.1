# Atributo de classe é compartilhado por todos os objetos
# Atributo de instância pertence a cada objeto individual

class Exemplo:
    atributo_classe = 10

    def __init__(self):
        self.atributo_instancia = 20

a = Exemplo()
b = Exemplo()

Exemplo.atributo_classe = 30

print(a.atributo_classe)
print(b.atributo_classe)

a.atributo_instancia = 50

print(a.atributo_instancia)
print(b.atributo_instancia)